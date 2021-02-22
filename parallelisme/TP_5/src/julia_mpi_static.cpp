#include "Array2D.hpp"
#include <complex>
#include <iostream>
#include <fstream>
#include <functional>
#include <mpi.h>
#include <vector>

// calcul la suite z = z*z+c jusqu'a ce que ||z||>bound
// retourne le nombre d'iterations jusqu'a divergence
int divergence(std::complex<double> z0, std::complex<double> c, double bound, int imax){
    std::complex<double> z = z0;
    for(int i=0; i<imax; i++){
        if(norm(z) > bound) return i;
        z = z*z + c;
    }
    return imax;
}

// convertir une coordonnee du domaine discret en corrdonnee dans le domaine complexe
std::complex<double> coord2cplx(const std::complex<double>& ll, const std::complex<double>& ur, int x, int y, Array2D<int>& d){
    std::complex<double> res( ll.real() + x*(ur.real() - ll.real())/d.sizeX(), -(ll.imag() + y*(ur.imag() - ll.imag())/d.sizeY()) );
    return res;
}

// calcul l'ensemble de julia
void julia(const std::complex<double>& ll, const std::complex<double>& ur, const std::complex<double>& c, int imax, Array2D<int>& d, int myRank, int split){
    for(int y=0; y<d.sizeY(); y++){
      if (y%split == myRank){
        for(int x=0; x<d.sizeX(); x++){
            d(x, y) = divergence( coord2cplx(ll, ur, x, y, d), c, 2.0, imax );
        }
      }
    }
}

// ecrit le domaine sous forme d'image pgm
void writePgm(Array2D<int>& d, int imax, std::string filename){
    std::ofstream file;
    file.open (filename);
    file << "P2" << std::endl;
    file << d.sizeX() << " " << d.sizeY() << std::endl;
    file << imax << std::endl;
    for(int y=0; y<d.sizeY(); y++){
        for(int x=0; x<d.sizeX(); x++){
            file << d(x, y) << " ";
        }
        file << std::endl;
    }
    file.close();
}

int main(int argc, char** argv){

    // initialisation des parametres
    std::complex<double> lowerLeft (std::stof(argv[1]), std::stof(argv[2]));
    std::complex<double> upperRight (std::stof(argv[3]), std::stof(argv[4]));
    std::complex<double> c(std::stof(argv[5]), std::stof(argv[6]));
    int imax = std::stoi(argv[7]);
    int dimX = std::stoi(argv[8]);
    int dimY = std::stoi(argv[9]);
    Array2D<int>domain(dimX, dimY);
    std::string filename(argv[10]);

    int myRank, nProc;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
    MPI_Comm_size(MPI_COMM_WORLD, &nProc);

    // repartition des donnees parmis les nProc
    julia(lowerLeft, upperRight, c, imax, std::ref(domain), myRank, nProc);
    std::cout << "task : "<<myRank << std::endl;
    //MPI_Gatherv(domainTask, dimX * dimYloc, MPI_INT,domain, dimYlocs.data(), startAt.data(), int, 0, MPI_COMM_WORLD);
    //writePgm(domain, imax, filename);

    // calcul de l'ensemble de julia
    // le domaine est passe via un std::ref, ici ce n'est pas utile
    // mais lors de la creation d'un thread, les objets sons passes par copie
    // std::ref permet de passer une reference au thread
    //julia(lowerLeft, upperRight, c, imax, std::ref(domain));

    // ecriture du resultat dans un fichier
    if (myRank == 0){
      writePgm(domain, imax, filename);
    }

    MPI_Finalize();
}
