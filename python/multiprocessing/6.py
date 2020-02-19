from concurrent.futures import ProcessPoolExecutor
import time

"""
クロージャーではなくシンプルな関数にした。すると動いた。
"""


def f(x):
    print(f"receive x={x}")
    time.sleep(2)
    return x + 1


with ProcessPoolExecutor() as executor:
    ret = executor.map(f, range(10))

for r in ret:
    print(r)
