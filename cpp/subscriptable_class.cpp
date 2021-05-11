#include <iostream>
#include <string>

using namespace std;

class A{
private:
  double v[10];
public:
  double& operator[](const int& i) {
    return v[i];
  }
};



int main(){
  A a;
  a[0] = 1;
  cout << a[0] << endl;
  return 0;
}
