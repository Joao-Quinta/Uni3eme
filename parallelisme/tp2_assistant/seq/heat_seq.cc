// On resout l'equation de la chaleur (de Laplace) sur un domaine regulier.
#include <iostream>
#include <iterator>
#include <fstream>
#include "Array2D.hpp"

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

  const int dimX = atoi(argv[1]);
  const int dimY = atoi(argv[2]);
  const int maxT = atoi(argv[3]);

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

  for (int iT=0; iT<maxT; iT++) {      // boucle principale : on fait maxT iterations
    for (int iY=1; iY<dimY-1; iY++) {  // on itere a l'interieur du domaine
      for (int iX=1; iX<dimX-1; iX++) {
        tmp(iX,iY) = 0.25*( heat(iX-1,iY) + heat(iX+1,iY)+
                            heat(iX,iY-1) + heat(iX,iY+1) );
      }
    }
    heat.unsafeSwap(tmp);              // Les deux matrices sont interverties (ceci ne fait que copier
                                       // deux pointeurs, ca ne coute donc pas trop de temps)
  }

  save(heat, "chaleur.dat");
}
