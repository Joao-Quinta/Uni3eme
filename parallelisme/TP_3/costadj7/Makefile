all: laplace_threads

laplace: src/heat_threads.cc src/Array2D.hpp src/Barrier.hpp
	mpiCC src/heat_threads.cc src/Array2D.hpp src/Barrier.hpp -o laplace -std=c++11

clean:
	rm -r *.o
