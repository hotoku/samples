#include <memory>
#include <iostream>


using namespace std;

int main(){
  const shared_ptr<int> x(new int(1));
  cout << *x << endl;
  *x = 10;
  cout << *x << endl;
  const shared_ptr<const int> y(new int(1));
  return 0;
}
