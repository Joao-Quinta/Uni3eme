#include <mpi.h>
#include <iostream>
#include <vector>

int main(int argc, char **argv) {
  int myRank, nProc;

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &nProc);

  MPI_Barrier(MPI_COMM_WORLD);
  double start = MPI_Wtime();

  std::vector<int> vector(100000000, 0);
  if(myRank == 0) {
    vector = std::vector<int>(100000000, 1);
    for (int i=1; i < nProc; i++){
      MPI_Send(vector.data(),vector.size(),MPI_INT,i,0,MPI_COMM_WORLD);
    }
  }
  else{
    MPI_Status status;
    MPI_Recv(vector.data(), vector.size(), MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
  }

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
