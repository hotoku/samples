#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main(){
  fs::path p("a/b/c.txt");

  std::cout << p.stem() << std::endl;
  std::cout << p.string() << std::endl;

  std::string s = p;

  return 0;
}


// Local Variables:
// flycheck-clang-language-standard: "c++17"
// flycheck-gcc-language-standard: "c++17"
// End:
