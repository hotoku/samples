import numpy as np


x = np.arange(10)
x[x < 3] = 100
print(x)
