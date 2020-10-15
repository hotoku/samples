#include<iostream>

using namespace std;

#define TYPEMAX(type) {                                                 \
    const unsigned long long temp = (1llu << (sizeof(type)*8 - 1)) - 1; \
    cout << #type << ": " << temp << endl;                              \
  }

#define UTYPEMAX(type) {                                                \
    const unsigned long long temp1 = (1llu << (sizeof(type)*8 - 1)) - 1; \
    const unsigned long long temp2 = (1llu << (sizeof(type)*8 - 1));    \
    cout << #type << ": " << temp1+temp2 << endl;                       \
  }


int main(){
  TYPEMAX(char);
  TYPEMAX(int);
  TYPEMAX(long long);
  UTYPEMAX(unsigned char);
  UTYPEMAX(unsigned int);
  UTYPEMAX(unsigned long long);
}
