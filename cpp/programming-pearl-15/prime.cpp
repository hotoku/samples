#include <iostream>

using namespace std;

bool isprime(int n){
  for(int i = 2; i*i <= n; i++){
    if(n%i == 0) return false;
  }
  return true;
}

int main(){
  for(int n = 40000; n > 0; --n){
    if(isprime(n)) {
      cout << n << endl;
      break;
    }
  }
}
