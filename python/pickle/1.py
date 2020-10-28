import pickle
import bz2

data = {}
for i in range(100000):
    data[i] = range(10000)

with open("1-1.dat", "wb") as f:
    pickle.dump(data, f)

with bz2.open("1-2.dat", "wb") as f:
    pickle.dump(data, f)

# -rw-r--r--   1 hotoku  staff  2468134 10 28 13:18 1-1.dat
# -rw-r--r--   1 hotoku  staff   297735 10 28 13:18 1-2.dat
