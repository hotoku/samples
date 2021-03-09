#include <string>
#include <iostream>

using namespace std;

int main(){
  if(strcmp("abc", "abc")){
    cout << "abc == abc: true" << endl;
  } else {
    cout << "abc == abc: false" << endl;
  }

  if(strcmp("abc", "abd")){
    cout << "abc == abd: true" << endl;
  } else {
    cout << "abc == abd: false" << endl;
  }
}

// strcmpは、両方の文字列が等しいとき 0 を返す
// 左が右より小さい時 < 0
// 左が右より大きい時 > 0
