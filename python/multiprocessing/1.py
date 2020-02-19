import multiprocessing as mp
import time


def f(x):
    print(f"receive {x}")
    time.sleep(2)
    return x + 1


with mp.Pool(4) as p:
    ret = p.map(f, range(4))

print(ret)
