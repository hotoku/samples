#!/usr/bin/env python


import apache_beam as beam



p = beam.Pipeline()

def read_line(l):
    l2 = l.split(",")
    return int(l2[0]), int(l2[1])

cnt = 0

def print_combined(*args, **kwargs):
    global cnt
    cnt += 1
    print(f"args={args}")
    print(f"kwargs={kwargs}")

(p
 | beam.io.ReadFromText("dat.csv")
 | beam.Map(read_line)
 | beam.CombinePerKey(print_combined)
)
 
p.run()
print(cnt)
