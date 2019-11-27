#!/usr/bin/env python


import apache_beam as beam



p = beam.Pipeline()

def read_line(l):
    l2 = l.split(",")
    return int(l2[0]), int(l2[1])

cnt = 0

def print_combined(it, *args, **kwargs):
    global cnt
    cnt += 1
    print(f"it={it} args={args} kwargs={kwargs}")
    return cnt

(p
 | beam.io.ReadFromText("dat.csv")
 | beam.Map(read_line)
 | beam.CombinePerKey(print_combined)
 | beam.Map(print)
)
 
p.run()
print(cnt)
