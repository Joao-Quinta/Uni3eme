#include <vector>
#include <cstdlib>

// simple classe pour un tableau 2D
template<class T>
class Array2D {
    std::vector<T> vector;
    size_t sX;
public:
    Array2D() : vector(0), sX(0) {}
    Array2D(size_t cols, size_t rows) : vector (cols*rows), sX(cols) {}
    Array2D(size_t cols, size_t rows, T init) : vector (cols*rows, init), sX(cols) {}
    T& operator()(size_t xCoord, size_t yCoord) {
        return vector.at(yCoord*sX+xCoord);
    }
    T* data(){ return vector.data(); }
    size_t sizeX(){ return sX;  }
    size_t sizeY(){ return vector.size()/sX;  }
    void resize(size_t c, size_t r){
        vector.resize(r*c);
        sX = c;
    }
    void unsafeSwap(Array2D<T> &otherArray){ otherArray.vector.swap(vector); }
    std::vector<T>& unsafeVector(){ return vector; }
};
