"""
classmethodで実験
"""


class A:
    def __init__(self, name):
        self.name = name

    def cached(f):
        cache = {}

        def ret(x):
            if x in cache:
                return cache[x]
            cache[x] = f(x)
            return cache[x]

        return ret

    @staticmethod
    @cached
    def f(x):
        print(f"f({x})")
        return x + 1


print(A.f(1))
print(A.f(1))
print(A.f(2))
print(A.f(2))
