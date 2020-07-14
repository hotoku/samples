def f(n):
    yield from g(n)


def g(n):
    yield from h(n)


def h(n):
    x = 0
    while x < n:
        yield x
        x += 1


for i in f(3):
    print(i)
