#include "easylogging++.h"

#include <iostream>
#include <string>



INITIALIZE_EASYLOGGINGPP

int f(int x){
  std::cout << "f" << x << std::endl;
  return x;
}

int main(int argc, char** argv){
  el::Loggers::configureFromGlobal("global.conf");

  // bool debug = false;
  // for (int i = 0; i < argc; i++) {
  //   if(strcmp(argv[i], "--debug")){
  //     debug = true;
  //   }
  // }
  // if(debug){
  //   el::Configurations conf;
  //   conf.set(el::Level::Debug,
  //            el::ConfigurationType::Enabled,
  //            "true");
  //   el::Loggers::reconfigureLogger("default", conf);
  // }

  LOG(DEBUG) << f(1);
  LOG(INFO) << f(2);
  return 0;
}
