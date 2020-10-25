// On resout l'equation de la chaleur (de Laplace) sur un domaine regulier.
#include <iostream>
#include <iterator>
#include <fstream>
#include "Array2D.hpp"
#include <mpi.h>
#include <vector>

// Sauvegarde d'une matrice dans un fichier texte
void save(Array2D<double> &matrix, std::string name) {
  std::ofstream file(name.c_str());
  for (int iY=0; iY<matrix.sizeY(); ++iY) {
     copy(&matrix.data()[iY*matrix.sizeX()], &matrix.data()[iY*matrix.sizeX()]+matrix.sizeX(),
          std::ostream_iterator<double>(file, " "));
     file << "\n";
  }
}

int main() {

  const int dimX = 200;
  const int dimY = 200;
  const int maxT = 40000;

  int myRank, nProc;
  Array<Int> nLinesProc, displacements;

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &nProc);

  // y a que le processus de rank 0 qui cree les matrices au debut
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
    int nLinesProc = dimY/nProc;
    int nLinesRestantes = dimY;
    displacements(0) = 0;
    for (int i=0; i<nProc; i++){
      if (nLinesProc <= nLinesRestantes){
        nLines(i) = nLinesProc
        nLinesRestantes = nLinesRestantes - nLinesProc
      } else {
        nLines(i) = nLinesRestantes
      }
    }
  }

  //mtn il faut scatter les matrices (les deux)
  MPI_Scatter(&heat,nLines,vector<int>,&heat,0,1);



  save(heat, "chaleur.dat");
}
