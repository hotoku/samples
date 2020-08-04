"""
基本的な使い方
"""

import re


r1 = re.match(r"a", "abc")
if r1:
    print("r1 match")


r2 = re.compile(r"a")
if r2.match("abc"):
    print("r2 match")


print(r2.sub("X", "abc"))
