from concurrent.futures import ThreadPoolExecutor
import time

"""
submitの使い方。submitだと、引数を指定できる。
"""


def f(x, y, z):
    print(f"{x} {y} {z}")
    time.sleep(2)
    return x + y + z


with ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(f, x, z=10, y=100)
        for x, y in zip(range(8), range(8))
    ]

for f in futures:
    print(f.result())
