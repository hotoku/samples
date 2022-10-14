from concurrent.futures import ProcessPoolExecutor
import time


def func(x):
    if x == 1:
        time.sleep(3)
    if x == 2:
        raise RuntimeError("x=2")
    return x + 1


def main():
    with ProcessPoolExecutor() as ex:
        fs = [ex.submit(func, x) for x in range(10)]

    # これは、2番目の要素の.resultを呼び出したところで例外が発生する
    # for f in fs:
    #     print(f.result())

    for f in fs:
        print(f.exception())


if __name__ == "__main__":
    main()
