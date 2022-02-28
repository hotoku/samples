#!/usr/bin/env python

"""
単純にiterateすると、列をなめる
"""

import pandas as pd

df = pd.DataFrame(dict(
    x=range(3),
    y=range(3)
))

for c in df:
    print(c)

"""
行をなめたい場合はiterrowsを使う
"""
for r in df.iterrows():
    print(r)
