all: laplace

laplace: src/laplace.cc src/Array2D.hpp
	mpiCC src/laplace.cc src/Array2D.hpp -o laplace -std=c++11

clean:
	rm -r *.o
