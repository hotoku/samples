from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timedelta


def f(n):
    print(n)


with ProcessPoolExecutor(max_workers=4) as ex:
    n = 1
    while n < 10:
        ex.submit(f, n)
        n += 1


def g(d):
    print(d)


with ProcessPoolExecutor(max_workers=4) as ex:
    d = datetime(2020, 1, 1)
    while not d == datetime(2020, 1, 10):
        ex.submit(g, d)
        d += timedelta(days=1)
