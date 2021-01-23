#include<iostream>
#include<vector>
#include<algorithm>
#include<iomanip>

using namespace std;


struct ans{
  int a, b, c;
};

vector<ans> vs;

int bya(ans a, ans b){
  return a.a - b.a;
}

int byc(ans a, ans b){
  return a.c - b.c;
}

ostream& operator<<(ostream& ost, ans x){
  return ost << x.a << " " << x.b << " " << x.c;
}

int main(){
  ans x = {1,2,3};
  ans y = {2,3,1};
  ans z = {3,1,2};
  ans k;
  vs.push_back(x);
  vs.push_back(y);
  vs.push_back(z);
  vs.push_back(k);
  for(auto v: vs){
    cout << v << endl;
  }

  cout << "--" << endl;

  sort(vs.begin(), vs.end(), bya);
  for(auto v: vs){
    cout << v << endl;
  }

  cout << "--" << endl;

  sort(vs.begin(), vs.end(), byc);
  for(auto v: vs){
    cout << v << endl;
  }
  return 0;
}
