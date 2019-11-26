#!/usr/bin/env python


import apache_beam as beam


def split_line(line):
    return line.split(",")


def run():
    p = beam.Pipeline()
    (p
     | "read" >> beam.io.ReadFromText("small.csv")
     | "split_line" >> beam.Map(split_line)
     | "print" >> beam.Map(print)
    )

    p.run()

if __name__ == "__main__":
    run()
