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
  }

    // nLinesProc = nombre de lignes par processus, ceil arrondit cette valeur en haut
    // exemple : 100 lignes en 3 proc, ceil(100/3) = 34
    // on met 34 lignes au premier (reste: 66)
    // on redivise 66 par 2 mtn -> 33, ceil(66/2) = 33
    // on met donc 33 a chaque processus restant

    // sizes ressemble donc a : {34,33,33}
    // displacements ressemble a : {0,34,67}

    // procSansL est le nb de proc sans lignes assignes
    int procSansL = nProc;
    // nb de lignes qu il restent a assigner
    int nLinesRestantes = dimY;
    // on assigne au premier proc dimY/nProc, et on arrondit en haut
    int nLinesProc = ceil(nLinesRestantes/procSansL);

    // std::vector<int> size;
    // std::vector<int> displacements;
    // on construit donc les deux vecteurs

    while (nLinesRestantes > 0) {

      if (displacements.size() == 0){
        // si premiere iteration -> displacements est vide, donc on push 0
        displacements.push_back(0);
      } else{
        // si pa 1ere itération -> dsplacements push les derniers elements de displacements + size
        displacements.push_back(displacements.back() + sizes.back());
      }
      sizes.push_back(nLinesProc);
      // on a assigne des lignes a un proc, donc on remet a jour les valeurs
      nLinesRestantes = nLinesRestantes - nLinesProc;
      procSansL = procSansL - 1;
      // on recalcule lignes par proc -> si on veut donner 100 a 3 ->
      // on fait ainsi {34,33,33} plutot que {34,34,32}
      if (procSansL > 0){
        nLinesProc = ceil(nLinesRestantes/procSansL);
      }
    }
    if (myRank == 0){
      printf("%d || %d || %d \n", sizes[0], sizes[1], sizes[2]);
      printf("%d || %d || %d \n", displacements[0], displacements[1], displacements[2]);
    }


  //mtn il faut scatter les matrices (les deux)
  //MPI_Scatter(&heat,nLines,vector<int>,&heat,0,1);
  MPI_Finalize();

}
