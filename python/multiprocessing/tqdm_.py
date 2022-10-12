import os
from concurrent.futures import ProcessPoolExecutor

from tqdm import tqdm


def func(n):
    if n == 2:
        return n

    else:
        return n + 1


def main():
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as ex:
        n = 10**5
        ret = list(tqdm(ex.map(func, range(n)), total=n))
    print("done")


if __name__ == "__main__":
    main()
