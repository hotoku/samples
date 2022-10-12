import os
from concurrent.futures import ProcessPoolExecutor


def func(n, m):
    return n + m


def func2(args):
    n, m = args
    return n + m


def main():
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as ex:
        # これはエラー。引数は全てiterableでないとだめ
        # ret = list(ex.map(func, range(10), range(10)))
        ret = list(ex.map(func, range(10), range(10)))
        print(ret)

        def constant(n):
            while True:
                yield n
        ret = list(ex.map(func2, zip(range(10), constant(10))))
        print(ret)


if __name__ == "__main__":
    main()
