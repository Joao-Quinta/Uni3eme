all: laplace

broadcastSimple: src/heat_p.cc src/Array2D.hpp
	mpiCC src/heat_p.cc src/Array2D.hpp -o laplace -std=c++11

clean:
	rm -r *.o
