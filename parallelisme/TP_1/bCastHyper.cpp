#include <mpi.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <cmath>

int main(int argc, char **argv) {
  int myRank, nProc, myStep;

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &nProc);

  MPI_Barrier(MPI_COMM_WORLD);
  double start = MPI_Wtime();

  // execution de l'algorithme
  std::vector<int> vector(100, 0);
  if (myRank == 0) {
    vector = std::vector<int>(100, 1);
    myStep = 0;
  }else{
    myStep = int(std::log2(myRank));
    MPI_Status status;
    MPI_Recv(vector.data(), vector.size(), MPI_INT, myRank-int(pow(2,myStep)), 0, MPI_COMM_WORLD, &status);
    myStep = myStep + 1;
  }
  while (int(pow(2,myStep)) < nProc) {
    MPI_Send(vector.data(),vector.size(),MPI_INT,myRank+int(pow(2,myStep)),0,MPI_COMM_WORLD);
    myStep = myStep + 1;
  }
  std::cout << "DONE: " << myRank <<" VECTOR : "<< vector.at(0)<< std::endl;

  // execution de l'algorithme

  MPI_Barrier(MPI_COMM_WORLD);
  double end = MPI_Wtime();

  if(myRank==0) std::cout << "temps de l'operation : " << end-start << "[s]" << std::endl;

  MPI_Finalize();
}

/*                              #### BROADCAST ####
#include <mpi.h>
#include <iostream>
#include <vector>

int main(int argc, char **argv) {
  int myRank, nProc;

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &nProc);

  std::vector<int> vector(100, 0);
  if(myRank == 0) vector = std::vector<int>(100, 1);

  MPI_Bcast( vector.data(), vector.size(), MPI_INT, 0, MPI_COMM_WORLD );

  std::cout << "myRank : " << myRank << ", value in the vector : " << vector.at(0) << std::endl;

  MPI_Finalize();
}
*/
