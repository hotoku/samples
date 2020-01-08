#!/usr/bin/env python


import subprocess as sp


command = ["ls", "-l"]
r = sp.run(command, stdout=sp.PIPE)

# sp.PIPEにはバイト列が入っているので、行ごとの文字列ではなく
# 1バイトごとに数字が表示される
for l in r.stdout:
    print(l)
