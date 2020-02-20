from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

"""
10.pyから、 ProcessPoolExecutorだけ残してみる。
これは動くぞ・・
"""


def f():
    s = 0
    while s < 1e8:
        s += 1
    return s


t3 = time.time()
with ProcessPoolExecutor(max_workers=4) as executor:
    futures = [
        executor.submit(f)
        for i in range(4)
    ]
for f in futures:
    print(f.result())
t4 = time.time()
print(f"process: {t4-t3}")
