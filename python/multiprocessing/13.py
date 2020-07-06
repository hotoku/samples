from concurrent.futures import ProcessPoolExecutor

"""
This does not work.
The function passed to ex.submit must not be a closure.
"""


def main():
    x = 10

    def f(n):
        print(n + x)

    for n in range(10):
        with ProcessPoolExecutor(max_workers=4) as ex:
            ex.submit(f, n)


main()
