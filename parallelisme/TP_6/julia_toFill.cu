#include "stdio.h"
#include <iostream>
#include "Array2D.hpp"
#include <fstream>
#include <chrono>


__device__ double2 cplxmult(double2 a, double2 b){
    return make_double2(a.x*b.x-a.y*b.y, a.x*b.y+a.y*b.x);
}

__device__ double2 cplxadd(double2 a, double2 b){
    return make_double2(a.x+b.x, a.y+b.y);
}

__device__ double norm(double2 a){
    return sqrt(a.x*a.x + a.y*a.y);
}

__...__ int divergence(double2 z0, double2 c, double bound, int imax){
    ...
}

__...__ double2 coord2cplx(double2 ll, double2 ur, int2 pos, int2 size){
    return ...;
}

// Device code
__...__ void julia(int* A, int2 size, double2 ll, double2 ur, double2 c, double bound, int imax )
{
    ...
}

void writePgm(Array2D<int>& d, int imax, std::string filename){
    std::ofstream file;
    file.open (filename);
    file << "P2" << std::endl;
    file << d.sizeX() << " " << d.sizeY() << std::endl;
    file << imax << std::endl;
    for(int y=0; y<d.sizeY(); y++){
        for(int x=0; x<d.sizeX(); x++){
            file << d(x, y) << " ";
        }
        file << std::endl;
    }
    file.close();
}

// Host code
int main(int argc, char** argv)
{
    int2 size = make_int2(std::atoi(argv[1]), std::atoi(argv[2]));
    double2 ll = make_double2(std::atof(argv[3]), std::atof(argv[4]));
    double2 ur = make_double2(std::atof(argv[5]), std::atof(argv[6]));
    double2 c = make_double2(std::atof(argv[7]), std::atof(argv[8]));
    double bound = std::atof(argv[9]);
    int imax = std::atoi(argv[10]);

    // Allocate vectors h_A, h_B and h_C in host memory
    Array2D<int> h_A(size.x, size.y);

    // Allocate vectors in device memory
    int* d_A;
    cudaMalloc(...);

    // Invoke kernel
    dim3 dimBlock(...);
    dim3 dimGrid(...);


    auto start = std::chrono::steady_clock::now();

    julia<<<dimGrid, dimBlock>>>(d_A, size, ll, ur, c, bound, imax);

    cudaDeviceSynchronize();
    auto end = std::chrono::steady_clock::now();

    auto diff = end - start;
    std::cout << "Computation time : " << std::chrono::duration <double, std::milli> (diff).count() << " ms" << std::endl;

    // Copy result from device memory to host memory
    // h_C contains the result in host memory

    start = std::chrono::steady_clock::now();

    cudaMemcpy(...);

    cudaDeviceSynchronize();
    end = std::chrono::steady_clock::now();
    diff = end - start;
    std::cout << "Copy time : " << std::chrono::duration <double, std::milli> (diff).count() << " ms" << std::endl;

    writePgm(h_A, imax, "julia.pgm");

    // Free device memory
    cudaFree(...);
}
