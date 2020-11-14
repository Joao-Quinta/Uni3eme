#include <iostream>
#include <thread>
#include <vector>
#include <atomic>

std::atomic<int> value;

void add(int val){
  // value = value + val; // Ne marche pas
  value += val;
}

void threadSafeAdd(int val){
  bool done = false;
  while(!done){
    int expected = value;
    int newval = expected+val;
    done = atomic_compare_exchange_weak(&value, &expected, newval);
  }
}

void adder(int val){
  for(int i=0; i<val; i++){
    add(1);
  }
}

void threadSafeAdder(int val){
  for(int i=0; i<val; i++){
    threadSafeAdd(1);
  }
}

int main(){

  value = 0;
  std::vector<std::thread> threads;
  for(int i=0; i<10; i++) threads.push_back(std::thread(adder, 10000));
  for(int i=0; i<10; i++) threads[i].join();
  std::cout << value << std::endl;

  threads.clear();
  value = 0;
  for(int i=0; i<10; i++) threads.push_back(std::thread(threadSafeAdder, 10000));
  for(int i=0; i<10; i++) threads[i].join();
  std::cout << value << std::endl;

}
