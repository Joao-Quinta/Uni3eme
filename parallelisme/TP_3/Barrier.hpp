#include <mutex>
#include <condition_variable>

class Barrier{

private:

  std::mutex m;
  std::condition_variable cv;
  int generation;
  int waiting;
  int threshold;

public:

  Barrier(int n){
    generation = 0;
    waiting = 0;
    threshold = n;
  }

  Barrier(){
    generation = 0;
    waiting = 0;
    threshold = 0;
  }

  void init(int n){
    waiting = 0;
    threshold = n;
  }

  void wait(){
    auto myGeneration = generation;
    std::unique_lock<std::mutex> lk(m);
    waiting++;
    if(waiting == threshold){
      generation++;
      waiting = 0;
      cv.notify_all();
    }
    else{
      while(myGeneration == generation) cv.wait(lk);
    }
  }

};
