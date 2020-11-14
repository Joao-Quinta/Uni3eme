#include <mpi.h>
#include <iostream>
#include <vector>
#include <cassert>

const int nbEnvois = 8;

int main(int argc, char **argv) {
  int myRank, nProc;
  MPI_Status status;
  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &nProc);

  assert(nProc==2);

  int size = 1;
  for (int iSize=1; iSize<nbEnvois; ++iSize) {
    std::vector<int> buffer(size);

    if (myRank == 0) {
      std::cout << "Envoi d\'un message de " << size << " entiers" << std::endl;
      MPI_Send(buffer.data(), size, MPI_INT, 1, 0, MPI_COMM_WORLD);
      MPI_Recv(buffer.data(), size, MPI_INT, 1, 0,MPI_COMM_WORLD, &status);
    }
    else {
      MPI_Send(buffer.data(), size, MPI_INT, 0, 0, MPI_COMM_WORLD);
      MPI_Recv(buffer.data(), size, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
    }
    size *= 10;
  }

  if (myRank == 0) {
    std::cout << "Fin des envois" << std::endl;
  }

  MPI_Finalize();
}
