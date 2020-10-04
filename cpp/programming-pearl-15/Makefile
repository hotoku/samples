.phony: map hash all


all: map hash


map: map.out pg10.txt
	time ./$< < pg10.txt


hash: hash.out pg10.txt
	time ./$< < pg10.txt


%.out: %.cpp
	g++ -O3 --std=c++11 -o $@ $<


pg10.txt:
	curl http://www.gutenberg.org/cache/epub/10/pg10.txt > $@
