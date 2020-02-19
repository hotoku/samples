from concurrent.futures import ThreadPoolExecutor
import time

"""
ThreadPoolExecutorにしたら素直に動いた。
"""


def f(y):
    def g(x):
        print(f"receive x={x} y={y}")
        time.sleep(2)
        return x + y
    return g


g = f(100)
with ThreadPoolExecutor() as executor:
    ret = executor.map(g, range(4))

for r in ret:
    print(r)
