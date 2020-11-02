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

  const int dimX = atoi(argv[1]);
  const int dimY = atoi(argv[2]);
  const int maxT = atoi(argv[3]);

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
  Array2D<double> heatReceive(dimX, sizes[myRank], 1); // La matrice de la chaleur
  Array2D<double> tmpReceive(dimX, sizes[myRank], 0);  // Une matrice temporaire
  int tailleBufferRecu = dimX * sizes[myRank];


  if (myRank == 0){
    MPI_Scatterv(&heat(0,0), sizes.data(), displacements.data(),
                MPI_DOUBLE, &heatReceive(0,0), tailleBufferRecu,
                MPI_DOUBLE, 0, MPI_COMM_WORLD);
    MPI_Scatterv(&tmp(0,0), sizes.data(), displacements.data(),
                MPI_DOUBLE, &tmpReceive(0,0), tailleBufferRecu,
                MPI_DOUBLE, 0, MPI_COMM_WORLD);
  }else{
    MPI_Scatterv(NULL, NULL, NULL,
                MPI_DOUBLE, &heatReceive(0,0), tailleBufferRecu,
                MPI_DOUBLE, 0, MPI_COMM_WORLD);
    MPI_Scatterv(NULL, NULL, NULL,
                MPI_DOUBLE, &heatReceive(0,0), tailleBufferRecu,
                MPI_DOUBLE, 0, MPI_COMM_WORLD);

  }
  /*
  for (int i = displacements[myRank]; i < displacements[myRank] + sizes[myRank]; i++){
    //printf("my rank is %d  and my displacements is %d \n", myRank, displacements[myRank]);
    for (int j = 0; j < dimX; j++){
      int z = i - displacements[myRank];
      //printf("heatReceive : (%d , %d) = heat : (%d , %d)\n", j,z,j,i);
      heatReceive(j,z) = heat(j,i);
      tmpReceive(j,z) = heat(j,i);
    }
  }*/

  if (myRank == 0){
    for (int i = 0; i < dimY; i++){
      for(int j = 0; j < dimX; j++){
        printf(" %f ", heat(j,i));
      }printf("\n" );
    }
  }

  printf("my rank is : %d\n", myRank);
  for (int i = 0; i < sizes[myRank]; i++){
    for(int j = 0; j < dimX; j++){
      printf("%f ", heatReceive(j,i));
    }printf("\n" );
  }printf("\n" );

  std::vector<double> vectorEnvoieBot;
  std::vector<double> vectorRecuBot(dimX,0);
  std::vector<double> vectorEnvoieTop;
  std::vector<double> vectorRecuTop(dimX,0);

  for (int iter = 0; iter < maxT; iter ++){
    int j = sizes[myRank] - 1;
    for (int i = 0; i < dimX; i++){
      vectorEnvoieBot.push_back(heatReceive(i,j));
    }
    j = 0;
    for (int i = 0; i < dimX; i++){
      vectorEnvoieTop.push_back(heatReceive(i,j));
    }
    MPI_Status status;
    if (myRank == 0){
      MPI_Sendrecv(vectorEnvoieBot.data(), vectorEnvoieBot.size(),
                  MPI_DOUBLE, myRank + 1, 0, vectorRecuTop.data(),
                  vectorRecuTop.size(), MPI_DOUBLE, MPI_ANY_SOURCE,
                  0, MPI_COMM_WORLD, &status);
    } else if (myRank == nProc-1){
      MPI_Sendrecv(vectorEnvoieTop.data(), vectorEnvoieTop.size(),
                  MPI_DOUBLE, myRank - 1, 0, vectorRecuBot.data(),
                  vectorRecuBot.size(), MPI_DOUBLE, MPI_ANY_SOURCE,
                  0, MPI_COMM_WORLD, &status);
    } else {
      MPI_Sendrecv(vectorEnvoieBot.data(), vectorEnvoieBot.size(),
                  MPI_DOUBLE, myRank + 1, 0, vectorRecuTop.data(),
                  vectorRecuTop.size(), MPI_DOUBLE, MPI_ANY_SOURCE,
                  0, MPI_COMM_WORLD, &status);
      MPI_Sendrecv(vectorEnvoieTop.data(), vectorEnvoieTop.size(),
                  MPI_DOUBLE, myRank - 1, 0, vectorRecuBot.data(),
                  vectorRecuBot.size(), MPI_DOUBLE, MPI_ANY_SOURCE,
                  0, MPI_COMM_WORLD, &status);

    }

    if (myRank == 0){
      for (int iY = 1; iY < sizes[myRank]; iY++){
        for (int iX = 1; iX < dimX - 1; iX++){
          if(iY == sizes[myRank] - 1){
            tmpReceive(iX,iY) = 0.25* (heatReceive(iX-1,iY) + heatReceive(iX+1,iY) + heatReceive(iX,iY-1) + vectorRecuBot[iX]);
          }else{
            tmpReceive(iX,iY) = 0.25* (heatReceive(iX-1,iY) + heatReceive(iX+1,iY) + heatReceive(iX,iY-1) + heatReceive(iX,iY+1));
          }
        }
      }
    }
    if (0 < myRank < nProc - 1){
      for (int iY = 0; iY < sizes[myRank]; iY++){
        for (int iX = 1; iX < dimX - 1; iX++){
          if(iY == sizes[myRank] - 1){
            tmpReceive(iX,iY) = 0.25* (heatReceive(iX-1,iY) + heatReceive(iX+1,iY) + heatReceive(iX,iY-1) + vectorRecuBot[iX]);
          }else if(iY == 0){
            tmpReceive(iX,iY) = 0.25* (heatReceive(iX-1,iY) + heatReceive(iX+1,iY) + heatReceive(iX,iY+1) + vectorRecuTop[iX]);
          }else{
            tmpReceive(iX,iY) = 0.25* (heatReceive(iX-1,iY) + heatReceive(iX+1,iY) + heatReceive(iX,iY-1) + heatReceive(iX,iY+1));
          }
        }
      }

    }
    if (myRank == nProc - 1){
      for (int iY = 0; iY < sizes[myRank] - 1; iY++){
        for (int iX = 1; iX < dimX - 1; iX++){
          if(iY == 0){
            tmpReceive(iX,iY) = 0.25* (heatReceive(iX-1,iY) + heatReceive(iX+1,iY) + heatReceive(iX,iY+1) + vectorRecuTop[iX]);
          }else{
            tmpReceive(iX,iY) = 0.25* (heatReceive(iX-1,iY) + heatReceive(iX+1,iY) + heatReceive(iX,iY-1) + heatReceive(iX,iY+1));
          }
        }
      }
    }
    heatReceive.unsafeSwap(tmpReceive);
  }
  printf("my rank is : %d\n", myRank);
  for (int i = 0; i < sizes[myRank]; i++){
    for(int j = 0; j < dimX; j++){
      printf("%f ", heatReceive(j,i));
    }printf("\n" );
  }printf("\n" );

  MPI_Gatherv(&heatReceive, tailleBufferRecu, MPI_DOUBLE, &heat,
                sizes.data(), displacements.data(), MPI_DOUBLE,
                0, MPI_COMM_WORLD);
  if (myRank == 0){
    save(heat, "chaleur.dat");
  }

  MPI_Finalize();
}

/*
// ECHANGE VECTORS ENTRE PROC
//for (int ite = 0; ite < maxT; )

if (myRank == 0){
  MPI_Send(vectorEnvoieBot.data(), dimX, MPI_DOUBLE, 1, 1, MPI_COMM_WORLD);
  MPI_Status status;
  MPI_Recv(vectorRecuBot.data(), dimX, MPI_DOUBLE, 1, 2, MPI_COMM_WORLD, &status);
}
if (0 < myRank < nProc - 1){
  MPI_Status status;
  MPI_Recv(vectorRecuTop.data(), dimX, MPI_DOUBLE, myRank - 1, 1, MPI_COMM_WORLD, &status);
  MPI_Send(vectorEnvoieTop.data(), dimX, MPI_DOUBLE, myRank - 1, 2, MPI_COMM_WORLD);
  MPI_Send(vectorEnvoieBot.data(), dimX, MPI_DOUBLE, myRank + 1, 1, MPI_COMM_WORLD);
  MPI_Recv(vectorRecuBot.data(), dimX, MPI_DOUBLE, myRank + 1, 2, MPI_COMM_WORLD, &status);
}
if (myRank == nProc - 1){
  MPI_Status status;
  MPI_Recv(vectorRecuTop.data(), dimX, MPI_DOUBLE, myRank - 1, 1, MPI_COMM_WORLD, &status);
  MPI_Send(vectorEnvoieTop.data(), dimX, MPI_DOUBLE, myRank - 1, 2, MPI_COMM_WORLD);
}
*/