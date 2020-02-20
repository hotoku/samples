from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

"""
9.pyとほとんど同じ内容だが、processの結果を表示しようとすると、プログラムが停止しなくなる。
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
for f in futures:
    print(f.result())
t2 = time.time()
print(f"thread: {t2-t1}")


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
