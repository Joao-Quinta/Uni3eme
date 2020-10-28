all: laplace

laplace: heat_p.cc Array2D.hpp
	mpiCC heat_p.cc Array2D.hpp -o laplace -std=c++11

clean:
	rm -r *.o
