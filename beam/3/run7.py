#!/usr/bin/env python


import apache_beam as beam



p = beam.Pipeline()

def read_line(l):
    l2 = l.split(",")
    return int(l2[0]), int(l2[1])


cnt = dict(
    mysum=0,
    myprint=0
)
def mysum(it, *args, **kwargs):
    cnt["mysum"] += 1
    return sum(it)

def myprint(l):
    cnt["myprint"] += 1
    print(l)

(p
 | beam.io.ReadFromText("dat.csv")
 | beam.Map(read_line)
 | beam.CombinePerKey(mysum)
 | beam.Map(myprint)
)
 
p.run()
print(f"cnt={cnt}")
