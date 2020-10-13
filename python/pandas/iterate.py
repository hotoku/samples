#!/usr/bin/env python

"""
単純にiterateすると、列をなめる
"""

import pandas as pd

df = pd.DataFrame(dict(
    x=range(3),
    y=range(3)
))

for r in df:
    print(r)
