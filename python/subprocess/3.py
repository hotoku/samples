#!/usr/bin/env python


import subprocess as sp
from io import StringIO

command = ["ls", "-l"]
r = sp.run(command, stdout=sp.PIPE)
print("decondig..")
s = r.stdout.decode("utf-8")  # バイト列は.decodeで文字列に変換できる
print(s)
