#include <random>
#include <iostream>

using namespace std;

int main(){
  int seed1 = 0, seed2 = 0, seed3 = 1;
  mt19937 e1(seed1), e2(seed2), e3(seed3);
  uniform_real_distribution<double> generator(0, 1);

  for(int i = 0; i < 10; i++){
    cout << generator(e1) << ", "
         << generator(e2) << ", "
         << generator(e3) << endl;
  }
}
