def f(n):
    for i in range(n):
        yield i


def g(n):
    for i in range(n):
        yield i


def h(n):
    yield from f(n)
    yield from g(n)


for i in h(3):
    print(i)
