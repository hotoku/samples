#include <iostream>
#include <string>

using namespace std;

class A{
public:
  double operator()(const double& x) {
    return x + 1;
  }
  string operator()(const string& s){
    return s + "a";
  }
};



int main(){
  A a;
  cout << a(10) << endl;
  cout << a("x") << endl;
  return 0;
}
