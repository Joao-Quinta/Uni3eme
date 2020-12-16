all: julia

julia_mpi_simple: src/julia.cu src/Array2D.hpp
	nvcc src/julia.cu src/Array2D -std=c++11 -o julia

clean:
	rm -r *.o
