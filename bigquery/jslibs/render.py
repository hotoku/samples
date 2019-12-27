#!/usr/bin/env python


import logging
import re
import argparse
import jinja2 as j2
import sys
import subprocess as sp


parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="+")
args = parser.parse_args()


template = j2.Environment(loader=j2.FileSystemLoader(
    ".")).get_template("create.jinja.sql")
list_ = []
for f in args.files:
    proc = sp.Popen(["./gj2bqgeo.py", f], stdout=sp.PIPE)
    b = proc.stdout.__next__()
    s = b.decode("utf-8").strip()
    d = dict(
        name=re.sub(r"\.json$", "", f),
        polygon=s
    )
    list_.append(d)

data = dict(
    list_=list_
)
print(template.render(data))
