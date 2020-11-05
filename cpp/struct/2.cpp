#include <iostream>

struct obj {
  int x;
  int y;
};

using namespace std;

obj f(){
  return {
    1, 10
  };
}

int main(){
  auto x = f();
  cout << x.x << "," << x.y << endl;
}
