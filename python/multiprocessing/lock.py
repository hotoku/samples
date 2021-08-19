from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
import time
import multiprocessing


def do_f(x, y):
    print(f"{datetime.now()}: do_f x={x}, y={y}")
    time.sleep(3)
    return x + y


def f(x, y, lock):
    print(f"{datetime.now()}: f x={x}, y={y}")
    with lock:
        return do_f(x, y)


m = multiprocessing.Manager()
lock = m.Lock()

with ProcessPoolExecutor(max_workers=4) as ex:
    fs = [
        ex.submit(f, i, 1, lock) for i in range(3)
    ]

res = [f.result() for f in fs]

print(res)
