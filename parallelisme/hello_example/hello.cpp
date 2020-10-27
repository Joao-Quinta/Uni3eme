/**/
#include <mpi.h>
#include <iostream>
#include <vector>

int main(int argc, char **argv) {
  int myRank, nProc;

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &nProc);
  std::vector<int> v;


  if(myRank == 0){
    std::cout << "I'm process " << myRank << " I have yet to receive any message" << std::endl;
    int sumTot = 0;
    //for(int i=0; i<v.size(); i++) v[i] = i;
    for (int i=1; i < nProc; i++){
      int sumH = 0;
      MPI_Status status;
      MPI_Recv(&sumH, 1, MPI_INT, i, 0, MPI_COMM_WORLD, &status);
      sumTot = sumTot + sumH;
      //std::cout << "I'm process " << myRank << " I have received a message from :" << i << std::endl;
    }

    std::cout << "I'm process " << myRank << " I have received all message, sum is :" << sumTot << std::endl;

  }
  else {
    v.assign(10, myRank);
    int sum = 0;
    for(auto i: v) sum += i;
    std::cout << "Hello, I'm process " << myRank << " and the sum of my vector is " << sum << std::endl;
    MPI_Send(&sum, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
  }

  MPI_Finalize();
}
/**/

/*
#include <mpi.h>
#include <iostream>
#include <vector>

int main(int argc, char **argv) {
  int myRank, nProc;

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &nProc);

  std::vector<int> v(10, 0);

  if(myRank == 0){
    for(int i=0; i<v.size(); i++) v[i] = i;
    std::cout << "I'm process 0 and I'm sending my vector" << std::endl;
    MPI_Send(v.data(), v.size(), MPI_INT, 1, 0, MPI_COMM_WORLD);
  }
  else if(myRank == 1){
    MPI_Status status;
    std::cout << "I'm process 1, last element of my vector before receive is " << v.back() << std::endl;
    MPI_Recv(v.data(), v.size(), MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
    std::cout << "I'm process 1, last element of my vector after receive is " << v.back() << std::endl;
  }
  else{
    std::cout << "I'm process " << myRank << " I have nothing to do" << std::endl;
  }

  MPI_Finalize();
}
*/
/*
#include <mpi.h>
#include <iostream>
#include <vector>

int main(int argc, char **argv) {
  int myRank, nProc;

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &nProc);

  std::vector<int> v;
  v.assign(10, myRank);
  int sum = 0;
  for(auto i: v) sum += i;

  std::cout << "Hello, I'm process" << myRank << " and the sum of my vector is " << sum << std::endl;

  MPI_Finalize();
}
*/

/*
#include <mpi.h>
#include <iostream>

int main(int argc, char **argv) {
  int myRank, nProc;

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
  MPI_Comm_size(MPI_COMM_WORLD, &nProc);

  std::cout << "Hello, I'm process" << myRank << std::endl;
  std::cout << "There is " << nProc << " processes" << std::endl;

  MPI_Finalize();
}
*/
