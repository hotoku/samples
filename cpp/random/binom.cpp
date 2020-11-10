#include <random>

using namespace std;

int main(){
  static mt19937 engine(0);
  binomial_distribution<int> p1(-1, 0.1);
  const int x = p1(engine); // ここで値が返ってこなくなる
  return 0;
}
