from concurrent.futures import ThreadPoolExecutor


def f(x):
    print(x)


with ThreadPoolExecutor(max_workers=20) as ex:
    ex.map(f, range(100))
