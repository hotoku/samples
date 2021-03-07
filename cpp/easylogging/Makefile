srcs := $(shell ls *.cpp)

debug: a.out
	./a.out --debug

info: a.out
	./a.out

a.out: $(srcs)
	g++ -std=c++14 easylogging++.cpp 1.cpp
