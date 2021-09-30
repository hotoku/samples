import pandas as pd

df1 = pd.DataFrame(dict(
    id=[1, 1, 1]
))

df2 = df1.copy()
print(pd.concat([df1, df2]))
