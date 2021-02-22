all: laplace_threads

laplace_threads: src/heat_threads.cc src/Array2D.hpp src/Barrier.hpp
	g++ src/heat_threads.cc src/Array2D.hpp src/Barrier.hpp -o laplace_threads -std=c++11 -pthread

clean:
	rm -r *.o
