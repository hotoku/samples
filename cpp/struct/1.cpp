#include<iostream>


struct Node {
  int a, b;
  bool operator<(Node& y){
    return this->a != y.a ? this->a - y.a > 0: this->b - y.b > 0;
  }
};

int main(){
  return 0;
}
