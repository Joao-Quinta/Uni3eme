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

  const int dimX = 7;
  const int dimY = 6;
  const int maxT = 4000;

  int myRank, nProc;
  std::vector<int> sizes;
  std::vector<int> displacements;

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &nProc);

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

  int procSansL = nProc;
  int nLinesRestantes = dimY;
  int nLinesProc = ceil(nLinesRestantes/procSansL);


  while (nLinesRestantes > 0) {
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
  }
  Array2D<double> heatReceive(dimX, sizes[myRank], 0); // La matrice de la chaleur
  Array2D<double> tmpReceive(dimX, sizes[myRank], 0);  // Une matrice temporaire

  int tailleBufferRecu = dimX * sizes[myRank];

  //MPI_Scatterv(&heat, sizes.data(), displacements.data(), MPI_DOUBLE, &heatReceive,tailleBufferRecu, MPI_DOUBLE, 0, MPI_COMM_WORLD);

  //std::cout << "I'm process " << myRank << " and there are "<< nProc << " procs" <<std::endl;
  if (myRank == 0){
    for (int i = 0; i<dimY; i++){
      for(int j = 0; j < dimX; j++){
        printf(" %f ", heat(j,i));
      }printf("\n" );
    }
  }
  // printf("my rank is %d  and my displacements is %d \n", myRank, displacements[myRank]);
  // print elements recus par chaque

  if(myRank > 0){
    MPI_Status status;
    int b;
    MPI_Recv(&b, 1, MPI_INT, myRank-1, 0, MPI_COMM_WORLD, &status);
  }

  for (int i = displacements[myRank]; i < displacements[myRank] + sizes[myRank]; i++){
    //printf("my rank is %d  and my displacements is %d \n", myRank, displacements[myRank]);
    for (int j = 0; j < dimX; j++){
      int z = i - displacements[myRank];
      //printf("heatReceive : (%d , %d) = heat : (%d , %d)\n", j,z,j,i);
      heatReceive(j,z) = heat(j,i);
    }
  }
  printf(" my rank is : %d\n", myRank);
  for (int i = 0; i< sizes[myRank]; i++){
    for(int j = 0; j < dimX; j++){
      printf(" %f ", heatReceive(j,i));
    }printf("\n" );
  }
  if (myRank<nProc-1){
    int b = 1;
    MPI_Send(&b, 1, MPI_INT, myRank+1, 0, MPI_COMM_WORLD);
  }

  vectorEnvoieTop = std::vector<int>(dimX, 0);
  vectorRecuTop = std::vector<int>(dimX, 0);
  vectorEnvoieBot = std::vector<int>(dimX, 0);
  vectorRecuBot = std::vector<int>(dimX, 0);

  MPI_Finalize();

}

/*
// print displacements and sizes
if (myRank == 0){
  for (int i = 0; i < displacements.size(); i++){
    printf("%d - ", displacements[i]);
  }
  printf("\n");
  for (int i = 0; i < displacements.size(); i++){
    printf("%d - ", sizes[i]);
  }
  printf("\n");
}
*/
