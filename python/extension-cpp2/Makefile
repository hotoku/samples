.PHONY: test build debug


all: test


build:
	python setup.py build


test: build
	python test.py


debug: a.out
	./$<


a.out: hoge.cpp
	g++ -I /usr/local/anaconda3/include/python3.8 -D HOTOKU_DEBUG $<
