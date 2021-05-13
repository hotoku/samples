#include <iostream>
#include <unordered_map>




class State{
public:
  virtual std::size_t hash() const {
    return 1;
  };

  bool operator==(const State& other) const {
    return true;
  }
};

namespace std{
  template <>
  struct hash<State> {
    size_t operator()(const State& state) const {
      return state.hash();
    }
  };
}

class ValueFunction{
  std::unordered_map<State, double> map;
public:
  virtual double operator()(const State& state) const;
  virtual double update(const State& state, const double& newValue);
};

double ValueFunction::operator()(const State& state) const {
  auto p = map.find(state);
  double ret = 0;
  if(p != map.end()){
    ret = p->second;
  }
  return ret;
}

double ValueFunction::update(const State &state, const double& newValue){
  auto p = map.find(state);
  double ret = 0;
  if(p != map.end()){
    ret = p->second;
  }
  map[state] = newValue;
  return ret;
}

int main(){
  ValueFunction vf;
  State s;
  vf.update(s, 1.11);
  std::cout << vf(s) << std::endl;
  return 0;
}
