def f(n):
    if n == 0:
        yield n
    else:
        yield from f(n-1)
        yield n


for i in f(10):
    print(i)
