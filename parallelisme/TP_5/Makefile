all: julia_mpi_simple julia_mpi_static

julia_mpi_simple: src/julia_mpi_simple.cpp src/Array2D.hpp
	mpiCC src/julia_mpi_simple.cpp src/Array2D.hpp -o julia_mpi_simple -std=c++11

julia_mpi_static: src/julia_mpi_static.cpp src/Array2D.hpp
	mpiCC src/julia_mpi_static.cpp src/Array2D.hpp -o julia_mpi_static -std=c++11

clean:
	rm -r *.o
