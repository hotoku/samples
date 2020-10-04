#include <iostream>
#include <map>
#include <sys/time.h>

using namespace::std;

struct timeval s;
struct timeval e;

int main(int argc, char** argv){
  gettimeofday(&s, NULL);
  string buf;
  map<string, int> m;
  while (cin >> buf){
    m[buf]++;
  }
  gettimeofday(&e, NULL);
  cout << (e.tv_sec * 1e6 + e.tv_usec) - (s.tv_sec * 1e6 + s.tv_usec) << endl;
  for(auto it = m.begin(); it != m.end(); ++it){
    cout << "line: " << it->first << " " << it->second << endl;
  }
  gettimeofday(&e, NULL);
  cout << (e.tv_sec * 1e6 + e.tv_usec) - (s.tv_sec * 1e6 + s.tv_usec) << endl;
  return 0;
}
