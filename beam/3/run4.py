#!/usr/bin/env python


import apache_beam as beam



p = beam.Pipeline()

def read_line(l):
    l2 = l.split(",")
    return (l2[0], int(l2[1])), int(l2[2])


(p
 | beam.io.ReadFromText("dat3.csv")
 | beam.Map(read_line)
 | beam.CombinePerKey(sum)
 | beam.Map(print)
)
 
p.run()

