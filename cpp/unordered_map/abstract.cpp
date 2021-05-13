#include <iostream>
#include <unordered_map>




template <class State> class ValueFunction{
  std::unordered_map<State, double> map;
public:
  double operator()(const State& state) const;
  double update(const State& state, const double& newValue);
};

template <class State> double ValueFunction<State>::operator()(const State& state) const{
  auto p = map.find(state);
  if(p == map.end()){
    throw "ValueFunction::operator(): bad input";
  }
  return p->second;
}

template <class State> double ValueFunction<State>::update(const State& state, const double& newValue){
  auto p = map.find(state);
  double ret = 0;
  if(p != map.end()){
    ret = p->second;
  }
  map[state] = newValue;
  return ret;
}

class State{
public:
  const int v;

  State(const int v_): v(v_) {}

  bool operator==(const State& other) const {
    return v == other.v;
  }
};

namespace std {
  template <>
  struct hash<State>{
    size_t operator()(const State& s) const {
      return hash<int>()(s.v);
    }
  };
}

int main(){
  ValueFunction<State> vf;
  State s(1);
  vf.update(s, 1.11);
  std::cout << vf(s) << std::endl;
  return 0;
}
