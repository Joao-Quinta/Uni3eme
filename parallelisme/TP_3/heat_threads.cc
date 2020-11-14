// On resout l'equation de la chaleur (de Laplace) sur un domaine regulier.
#include <iostream>
#include <iterator>
#include <fstream>
#include <mutex>
#include <math.h>
#include <thread>
#include "Array2D.hpp"
#include "Barrier.hpp"


Barrier barrier;
Array2D<double> heat(1,1,0);
Array2D<double> tmp(1,1,0);

// Sauvegarde d'une matrice dans un fichier texte
void save(Array2D<double> &matrix, std::string name) {
  std::ofstream file(name.c_str());
  for (int iY=0; iY<matrix.sizeY(); ++iY) {
     copy(&matrix.data()[iY*matrix.sizeX()], &matrix.data()[iY*matrix.sizeX()]+matrix.sizeX(),
          std::ostream_iterator<double>(file, " "));
     file << "\n";
  }
}

void laplaceFunction(int yStart,int yNumberLines,int iterations, int xMax, int id){
  for (int iT=0; iT<iterations; iT++) {
    for (int yi=yStart; yi < (yStart + yNumberLines); yi++){
      for (int xi=1; xi < (xMax - 1); xi++){
        tmp(xi,yi) = 0.25*(heat(xi-1,yi) + heat(xi+1,yi) + heat(xi,yi-1) + heat(xi,yi+1));
      }
    }
    // double use ob barrier, 1st to make sure every thread computed their lines
    barrier.wait();
    // the second so everyone correctly waits for the unsafeSwap
    if(id == 0){
      heat.unsafeSwap(tmp);
    }
    barrier.wait();
  }
}

int main(int argc,char **argv) {

  const int dimX = atoi(argv[1]);
  const int dimY = atoi(argv[2]);
  const int maxT = atoi(argv[3]);
  const int nProc = atoi(argv[4]);

  heat.resize(dimX, dimY);
  tmp.resize(dimX, dimY);
  barrier.init(nProc);

  // we initialize the matrices values
  for (int iX=0; iX<dimX; iX++) {      // conditions aux bords:
      heat(iX,0) = 0;                 // 0 en haut
      heat(iX,dimY-1) = 1;            // 1 en bas
      tmp(iX,0) = 0;                  // 0 en haut
      tmp(iX,dimY-1) = 1;             // 1 en bas
  }
  for (int iY=0; iY<dimY; iY++) {
      heat(0,iY)      = 0.;           // 0 a gauche
      heat(dimX-1,iY) = 1.;           // 1 a droite
      tmp(0,iY)      = 0.;            // 0 a gauche
      tmp(dimX-1,iY) = 1.;            // 1 a droite
  }

  // sizes and displacements will hold the amount of lines for eche thread as well as the first line index
  std::vector<int> sizes;
  std::vector<int> displacements;

  int procSansL = nProc;
  int nLinesRestantes = dimY - 2;

  int nLinesProc = ceil(nLinesRestantes/procSansL);
  while (nLinesRestantes > 0) {
    if (displacements.size() == 0){
      displacements.push_back(1);
    } else{
      displacements.push_back(displacements.back() + sizes.back());
    }
    sizes.push_back(nLinesProc);
    nLinesRestantes = nLinesRestantes - nLinesProc;
    procSansL = procSansL - 1;
    if (procSansL > 0){
      nLinesProc = ceil(nLinesRestantes/procSansL);
    }
  }

  // we creat the threads that get as arguments their starting line and how many lines they compute
  std::vector<std::thread> threads;
  for(int i=1; i<nProc; i++)threads.push_back(std::thread(laplaceFunction,displacements[i], sizes[i], maxT, dimX, i));
  laplaceFunction(displacements[0], sizes[0], maxT, dimX, 0);
  for(int i=0; i < (nProc - 1); i++) threads[i].join(); // we join() the threads and save the matrix

  save(heat, "chaleur.dat");
}
