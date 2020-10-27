#include <mpi.h>
#include <iostream>
#include <vector>
#include <cassert>
 
int main(int argc, char **argv) {
  int myRank, nProc;
  MPI_Status status;
  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &nProc);
 
  assert(nProc==2);
 
  std::vector<int> send(1000000, myRank);
  std::vector<int> recv(1000000, -1);
 
  int dest=0;
  if(myRank==0) dest=1;
 
  MPI_Sendrecv(send.data(), send.size(), MPI_INT, dest, 999, recv.data(), recv.size(), MPI_INT,
               MPI_ANY_SOURCE, 999, MPI_COMM_WORLD, &status);
 
  std::cout << "I'm process " << myRank << " and last element of my received vector is " << recv.back() << std::endl;
 
  MPI_Finalize();
}
