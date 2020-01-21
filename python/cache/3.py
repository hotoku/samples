"""
クラス定義の中にデコレータがあるとどうなるか？
=> 2.pyと同じ挙動
"""


class A:
    def __init__(self, name):
        self.name = name

    def cached(f):
        cache = {}

        def ret(self, x):
            if x in cache:
                return cache[x]
            cache[x] = f(self, x)
            return cache[x]

        return ret

    @cached
    def f(self, x):
        print(f"name={self.name}")
        return x + 1


a1 = A(1)
a2 = A(2)


print(a1.f(1))
print(a1.f(1))
print(a1.f(2))
print(a1.f(2))

print(a2.f(1))
print(a2.f(1))
print(a2.f(2))
print(a2.f(2))
