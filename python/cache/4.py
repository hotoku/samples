def cached(f):
    cache = {}

    def ret(x):
        if x in cache:
            return cache[x]
        cache[x] = f(x)
        return cache[x]

    return ret


@cached
def g(x):
    print(f"g({x})")
    return x + 1


@cached
def h(x):
    print(f"h({x})")
    return x + 1


print(g(1))
print(g(1))
print(g(2))
print(g(2))
print(g(1))
print(g(1))
print(g(2))
print(g(2))


print(h(1))
print(h(1))
print(h(2))
print(h(2))
print(h(1))
print(h(1))
print(h(2))
print(h(2))
