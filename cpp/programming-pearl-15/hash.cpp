#include <iostream>
#include <map>
#include <sys/time.h>

using namespace::std;

struct timeval s;
struct timeval e;

typedef struct node *nodeptr;
typedef struct node {
  char* word;
  int count;
  nodeptr next;
} node;

#define MULT 31
#define NHASH 39989
nodeptr bin[NHASH];

unsigned int hash2(const char* p){
  unsigned int h = 0;
  for(; *p; p++){
    h = MULT * h + *p;
  }
  return h % NHASH;
}

void incword(const char* s){
  unsigned int h = hash2(s);
  for(nodeptr p = bin[h]; p; p = p->next){
    if(strcmp(p->word, s)==0){
      p->count++;
      return;
    }
  }
  nodeptr p = (nodeptr)malloc(sizeof(node));
  p->word = (char*)malloc(strlen(s)+1);
  strcpy(p->word, s);
  p->count = 1;
  p->next = bin[h];
  bin[h] = p;
}

int main(){
  gettimeofday(&s, NULL);
  string buf;
  map<string, int> m;
  while (cin >> buf){
    incword(buf.c_str());
  }

  gettimeofday(&e, NULL);
  cout << "hash: " << (e.tv_sec * 1e6 + e.tv_usec) - (s.tv_sec * 1e6 + s.tv_usec) << endl;

  for(int i = 0; i < NHASH; i++){
    for(nodeptr p = bin[i]; p; p = p->next){
      printf("line: %s %d\n", p->word, p->count);
    }
  }

  gettimeofday(&e, NULL);
  cout << "hash: " << (e.tv_sec * 1e6 + e.tv_usec) - (s.tv_sec * 1e6 + s.tv_usec) << endl;
  return 0;
}
