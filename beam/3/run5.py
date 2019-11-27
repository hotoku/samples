#!/usr/bin/env python


import apache_beam as beam



p = beam.Pipeline()

def read_line(l):
    l2 = l.split(",")
    return l2[0], int(l2[1])

cnt = 0

def print_combined(*args, **kwargs):
    global cnt
    cnt += 1
    print(f"args={args}, kwargs={kwargs}")

(p
 | beam.io.ReadFromText("dat2.csv")
 | beam.Map(read_line)
 | beam.GroupByKey()
 | beam.Map(print_combined)
)
 
p.run()
print(cnt)
