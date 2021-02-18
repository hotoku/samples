#include <iostream>


using namespace std;

int main(){
  size_t x = 0;
  int y = -1;
  if(x > y){
    cout << "x > y" << endl;
  } else {
    cout << "x <= y" << endl;
  }

  if((int)x > y){
    cout << "x > y" << endl;
  } else {
    cout << "x <= y" << endl;
  }
  return 0;
}
