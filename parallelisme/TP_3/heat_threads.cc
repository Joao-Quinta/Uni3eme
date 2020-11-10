// On resout l'equation de la chaleur (de Laplace) sur un domaine regulier.
#include <iostream>
#include <iterator>
#include <fstream>
#include <mutex>
#include <math.h>
#include <thread>
#include "Array2D.hpp"
#include "Barrier.hpp"


std::mutex m;
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

void laplaceFunction(int yStart,int yNumberLines,int iterations, int xMax,int id){
  for (int iT=0; iT<iterations; iT++) {
    m.lock();
    printf("SALUT id : %d ----- > %p\n",id, &heat(0,0));
    for (int yi=yStart; yi < (yStart + yNumberLines); yi++){
      //printf("MY ID : %d - ligne : %d -- \n",id, yi );
      for (int xi=1; xi < (xMax - 1); xi++){
        tmp(xi,yi) = 0.25*(heat(xi-1,yi) + heat(xi+1,yi) + heat(xi,yi-1) + heat(xi,yi+1));
        //printf("X: %d ---> %f -- %f -- %f -- %f  || ----> %f\n",xi,heat(xi-1,yi), heat(xi+1,yi), heat(xi,yi-1), heat(xi,yi+1),tmp(xi,yi));
      }
      /*
      m.lock();
      std::cout << "hi, this is my 'id' : " << id <<" i am doing line : "<< yi<<" at iteration : "<< iT << std::endl;
      m.unlock();
      */
    }
    m.unlock();
    barrier.wait();

    if(id == 0){
      /*
      printf("CHANGEMENT : \n" );
      for (int yi=0; yi < 10; yi++){
        for (int xi=0; xi < 10; xi++){
          printf("- %f -",tmp(xi,yi));
        }printf("\n");
      }
      */
      heat.unsafeSwap(tmp);
      /*
      printf("print it : %d \n", iT);
      for (int yi=0; yi < 10; yi++){
        for (int xi=0; xi < 10; xi++){
          printf("- %f -",heat(xi,yi));
        }printf("\n");
      }
      */
    }
    //heat.unsafeSwap(tmp);
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

  std::vector<int> sizes;
  std::vector<int> displacements;

  int procSansL = nProc;
  int nLinesRestantes = dimY - 2;
  printf("SALUT MAIN ----- > %p\n", &heat(0,0));

  printf("FIRST PRINT \n");
  for (int yi=0; yi < 10; yi++){
    for (int xi=0; xi < 10; xi++){
      printf("- %f -",heat(xi,yi));
    }printf("\n");
  }printf("\n");

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

  std::vector<std::thread> threads;
  for(int i=1; i<nProc; i++)threads.push_back(std::thread(laplaceFunction,displacements[i], sizes[i], maxT, dimX, i));
  laplaceFunction(displacements[0], sizes[0], maxT, dimX, 0);
  for(int i=0; i < (nProc - 1); i++) threads[i].join();

  printf("LAST PRINT \n");
  for (int yi=0; yi < 10; yi++){
    for (int xi=0; xi < 10; xi++){
      printf("- %f -",heat(xi,yi));
    }printf("\n");
  }printf("\n");

}

/*
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
*/
