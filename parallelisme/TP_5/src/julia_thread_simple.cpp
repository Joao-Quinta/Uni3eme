#include <iostream>
#include <iterator>
#include <fstream>
#include <math.h>
#include <thread>
#include <complex>
#include <functional>
#include "Array2D.hpp"

Array2D<double> domain(1,1,0);

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
std::complex<double> coord2cplx(const std::complex<double>& ll, const std::complex<double>& ur, int x, int y){
    std::complex<double> res( ll.real() + x*(ur.real() - ll.real())/domain.sizeX(), -(ll.imag() + y*(ur.imag() - ll.imag())/domain.sizeY()) );
    return res;
}

// calcul l'ensemble de julia
void julia(const std::complex<double>& ll, const std::complex<double>& ur, const std::complex<double>& c, int imax,int dimYTask,int startY){
    for(int y=0; y<dimYTask; y++){
        for(int x=0; x<domain.sizeX(); x++){
            domain(x, y + startY) = divergence( coord2cplx(ll, ur, x, y + startY), c, 2.0, imax );
        }
    }
}

// ecrit le domaine sous forme d'image pgm
void writePgm(int imax, std::string filename){
    std::ofstream file;
    file.open (filename);
    file << "P2" << std::endl;
    file << domain.sizeX() << " " << domain.sizeY() << std::endl;
    file << imax << std::endl;
    for(int y=0; y<domain.sizeY(); y++){
        for(int x=0; x<domain.sizeX(); x++){
            file << domain(x, y) << " ";
        }
        file << std::endl;
    }
    file.close();
}


int main(int argc,char **argv) {

  //lowerleft cc, uperright cc, and Complex vars
  std::complex<double> lowerLeft (std::stof(argv[1]), std::stof(argv[2]));
  std::complex<double> upperRight (std::stof(argv[3]), std::stof(argv[4]));
  std::complex<double> c(std::stof(argv[5]), std::stof(argv[6]));

  int imax = std::stoi(argv[7]);
  int dimX = std::stoi(argv[8]);
  int dimY = std::stoi(argv[9]);
  std::string filename(argv[10]);
  int nThreads = std::stoi(argv[11]);

  domain.resize(dimX, dimY);

  // sizes and displacements will hold the amount of lines for eche thread as well as the first line index
  std::vector<int> dimYlocs;
  std::vector<int> startAt;
  dimYlocs = std::vector<int>(nThreads,dimY / nThreads);
  int linesDistributed = (dimY / nThreads) * nThreads;

  int i = 0;
  while(linesDistributed != dimY){
      dimYlocs[i]++;
      linesDistributed++;
      i = (i+1)%nThreads;
  }

  for (int i = 0; i < dimYlocs.size();i++){
    if (i == 0){
      startAt.push_back(0);
    }
    else{
      startAt.push_back(startAt.back() + dimYlocs[i-1]);
    }
  }


  // we creat the threads that get as arguments their starting line and how many lines they compute
  std::vector<std::thread> threads;
  // const std::complex<double>& ll, const std::complex<double>& ur, const std::complex<double>& c, int imax, int dimYTask,int startY
  for(int i=1; i<nThreads; i++)threads.push_back(std::thread(julia, lowerLeft, upperRight, c, imax, dimYlocs[i], startAt[i]));
  julia(lowerLeft, upperRight, c, imax, dimYlocs[0], startAt[0]);
  for(int i=0; i < (nThreads - 1); i++) threads[i].join(); // we join() the threads and save the matrix

  writePgm(imax, filename);
}
