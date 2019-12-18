#!/usr/bin/env python


import argparse
import sys

parser = argparse.ArgumentParser(description="sample")
parser.add_argument("arg1")
parser.add_argument("arg2")
parser.add_argument("-a", action="store_true")

args = parser.parse_args()
print(args.arg1)
print(args.arg2)
print(args.a)
