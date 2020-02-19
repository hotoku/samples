import multiprocessing as mp
import time

"""
ダメな例。クロージャーは、multiprocessingで使えない。
Can't pickle ...というエラーになる。
"""


def f(y):
    def g(x):
        print(f"receive x={x} y={y}")
        time.sleep(2)
        return x + y
    return g


g = f(100)
with mp.Pool(4) as p:
    ret = p.map(g, range(4))

print(ret)
