all: laplace

laplace: laplace.cc Array2D.hpp
	mpiCC laplace.cc Array2D.hpp -o laplace -std=c++11

clean:
	rm -r *.o
