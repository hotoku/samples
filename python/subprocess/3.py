#!/usr/bin/env python


import subprocess as sp
from io import StringIO

command = ["python", "run.py"]
r = sp.run(command, stdout=sp.PIPE, stderr=sp.PIPE)
s = r.stdout.decode("utf-8")
print(s)
s = r.stderr.decode("utf-8")
print(s)
