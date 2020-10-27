// On resout l'equation de la chaleur (de Laplace) sur un domaine regulier.
#include <iostream>
#include <iterator>
#include <fstream>
#include "Array2D.hpp"
#include <mpi.h>
#include <math.h>
#include <vector>
#include <stdio.h>

// Sauvegarde d'une matrice dans un fichier texte
void save(Array2D<double> &matrix, std::string name) {
  std::ofstream file(name.c_str());
  for (int iY=0; iY<matrix.sizeY(); ++iY) {
     copy(&matrix.data()[iY*matrix.sizeX()], &matrix.data()[iY*matrix.sizeX()]+matrix.sizeX(),
          std::ostream_iterator<double>(file, " "));
     file << "\n";
  }
}

int main(int argc, char **argv) {

  const int dimX = 200;
  const int dimY = 100;
  const int maxT = 40000;

  int myRank, nProc;
  std::vector<int> sizes;
  std::vector<int> displacements;

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &nProc);
  std::cout << "I'm process " << myRank << " and there are "<< nProc << " procs" <<std::endl;

  if (myRank == 0){
    Array2D<double> heat(dimX, dimY, 0); // La matrice de la chaleur
    Array2D<double> tmp(dimX, dimY, 0);  // Une matrice temporaire

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
  }
  if (myRank == 0){
  int procSansL = nProc;
  int nLinesRestantes = dimY;
  int nLinesProc = ceil(nLinesRestantes/procSansL);

  while (nLinesRestantes > 0) {
    printf("numero de processeur sans ligne : %d || nLines par proc : %d || numero lignes restantes : %d \n", procSansL, nLinesProc, nLinesRestantes);
    if (displacements.size() == 0){
      displacements.push_back(0);
    } else{
      displacements.push_back(displacements.back() + sizes.back());
    }
    sizes.push_back(nLinesProc);
    nLinesRestantes = nLinesRestantes - nLinesProc;
    procSansL = procSansL - 1;
    if (procSansL > 0){
      nLinesProc = ceil(nLinesRestantes/procSansL);
  }
  printf("size 0 : %d ||  displacement 0 : %d  \n", sizes[0], displacements[0]);
  }
  printf("%d || %d || %d \n", sizes[0], sizes[1], sizes[2]);
  printf("%d || %d || %d \n", displacements[0], displacements[1], displacements[2]);

}


  //mtn il faut scatter les matrices (les deux)
  //MPI_Scatter(&heat,nLines,vector<int>,&heat,0,1);
  MPI_Finalize();

}
