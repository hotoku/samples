from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

"""
ThreadPoolExecutorとProcessPoolExecuterを比較してみる
"""


def f():
    s = 0
    while s < 1e8:
        s += 1
    return s


t1 = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [
        executor.submit(f)
        for i in range(4)
    ]
t2 = time.time()
print(f"thread: {t2-t1}")


t3 = time.time()
with ProcessPoolExecutor(max_workers=4) as executor:
    futures = [
        executor.submit(f)
        for i in range(4)
    ]
t4 = time.time()
print(f"process: {t4-t3}")
