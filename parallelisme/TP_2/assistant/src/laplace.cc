#include <iostream>
#include <iterator>
#include <fstream>
#include <cstdlib>
#include "Array2D.hpp"
#include "mpi.h"

int myRank;
int nProc;
MPI_Status status;

void save(Array2D<double> &matrix, std::string name) {
    std::ofstream file(name.c_str());
    for (int iY=0; iY<matrix.sizeY(); ++iY) {
        copy(&matrix.data()[iY*matrix.sizeX()], &matrix.data()[iY*matrix.sizeX()]+matrix.sizeX(),
                std::ostream_iterator<double>(file, " "));
        file << "\n";
    }
}

inline void update(Array2D<double>& heat, Array2D<double>& tmp){
    for (int iY=1; iY<heat.sizeY()-1; iY++) {
        for (int iX=1; iX<heat.sizeX()-1; iX++) {
            tmp(iX,iY) = 0.25*( heat(iX-1,iY) + heat(iX+1,iY) + heat(iX,iY-1) + heat(iX,iY+1));
        }
    }
    heat.unsafeSwap(tmp);
}

inline void exchange(Array2D<double>& heat){
    if(myRank%2==0){
        if(myRank != nProc-1) MPI_Sendrecv(heat.data()+heat.sizeX()*(heat.sizeY()-2), heat.sizeX(), MPI_DOUBLE, myRank+1, 1, heat.data()+heat.sizeX()*(heat.sizeY()-1), heat.sizeX(), MPI_DOUBLE, myRank+1, 1, MPI_COMM_WORLD, &status);
        if(myRank != 0) MPI_Sendrecv(heat.data()+heat.sizeX(), heat.sizeX(), MPI_DOUBLE, myRank-1, 1, heat.data(), heat.sizeX(), MPI_DOUBLE, myRank-1, 1, MPI_COMM_WORLD, &status);
    }
    else{
        if(myRank != 0) MPI_Sendrecv(heat.data()+heat.sizeX(), heat.sizeX(), MPI_DOUBLE, myRank-1, 1, heat.data(), heat.sizeX(), MPI_DOUBLE, myRank-1, 1, MPI_COMM_WORLD, &status);
        if(myRank != nProc-1) MPI_Sendrecv(heat.data()+heat.sizeX()*(heat.sizeY()-2), heat.sizeX(), MPI_DOUBLE, myRank+1, 1, heat.data()+heat.sizeX()*(heat.sizeY()-1), heat.sizeX(), MPI_DOUBLE, myRank+1, 1, MPI_COMM_WORLD, &status);
    }
}

int main(int argc, char **argv) {

    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
    MPI_Comm_size(MPI_COMM_WORLD, &nProc);

    int dimX = atoi(argv[1]);
    int dimY = atoi(argv[2]);
    int maxT = atoi(argv[3]);
    std::string filename(argv[4]);

    if(myRank == 0) {
        std::cout << "np" << std::endl;
        std::cout << nProc << std::endl;
        std::cout << "dimX, dimY" << std::endl;
        std::cout << dimX << ", " << dimY << std::endl;
    }

    // data repartition
    int dimYloc;
    std::vector<int> dimYlocs;
    if(myRank == 0){
        dimYlocs = std::vector<int>(nProc,dimY / nProc);
        int linesDistributed = (dimY / nProc) * nProc;
        int i = 0;
        while(linesDistributed != dimY){
            dimYlocs[i]++;
            linesDistributed++;
            i = (i+1)%nProc;
        }
    }
    MPI_Scatter(dimYlocs.data(), 1, MPI_INT, &dimYloc, 1, MPI_INT, 0, MPI_COMM_WORLD);

    int realSize = dimYloc*dimX;
    if(myRank == 0 || myRank == nProc-1) dimYloc++;
    else dimYloc += 2;

    Array2D<double> heat(dimX, dimYloc, 0);
    Array2D<double> tmp(dimX, dimYloc, 0);

    // boundary conditions
    if(myRank == 0){
        for (int iX=0; iX<dimX; ++iX) {
            heat(iX,0) = 0.;
            tmp(iX,0) = 0.;
        }
    }

    if(myRank == nProc-1){
        for (int iX=0; iX<dimX; ++iX) {
            heat(iX,dimYloc-1) = 1.;
            tmp(iX,dimYloc-1) = 1.;
        }
    }

    for (int iY=0; iY<dimYloc; ++iY) {
        heat(0,iY) = 0.;
        heat(dimX-1,iY) = 1.;
        tmp(0,iY) = 0.;
        tmp(dimX-1,iY) = 1.;
    }

    MPI_Barrier(MPI_COMM_WORLD);
    double start = MPI_Wtime();

    for (int iT=0; iT<maxT; ++iT) {
        exchange(heat);
        update(heat,tmp);
    }


    MPI_Barrier(MPI_COMM_WORLD);
    double end = MPI_Wtime();
    double computeTime = end-start;

    Array2D<double> res;
    double *bufSend = heat.data() + dimX;
    std::vector<int> sizes;
    std::vector<int> displs;

    if(myRank == 0){
        sizes.resize(nProc);
        res.resize(dimX,dimY);
        bufSend = heat.data();
    }

    MPI_Gather(&realSize, 1, MPI_INT, sizes.data(), 1, MPI_INT, 0, MPI_COMM_WORLD);

    if(myRank == 0){
        displs.push_back(0);
        for(int i=0; i<sizes.size()-1; i++){
            displs.push_back(displs[i]+sizes[i]);
        }
    }

    MPI_Gatherv(bufSend, realSize, MPI_DOUBLE, res.data(), sizes.data(), displs.data() , MPI_DOUBLE, 0, MPI_COMM_WORLD);
    double startWrite = MPI_Wtime();
    if(myRank == 0) save(res, filename);
    double endWrite = MPI_Wtime();

    if(myRank==0){
        std::cout << "computeTime, writeTime" << std::endl;
        std::cout << computeTime << ", " << endWrite-startWrite << std::endl;
        std::cout << "--------------------------------------------" << std::endl;
    }

    MPI_Finalize();

}
