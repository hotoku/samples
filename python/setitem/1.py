class A:
    def __init__(self):
        self._dic = {}

    def __setitem__(self, k, v):
        self._dic[k] = v

    def __getitem__(self, k):
        return self._dic[k]


a = A()
a["a"] = 1
print(a["a"])


class B:
    def __init__(self):
        self.array = [
            [0 for _ in range(10)]
            for _ in range(10)
        ]

    def __getitem__(self, pair):
        r, c = pair
        return self.array[r][c]

    def __setitem__(self, pair, v):
        r, c = pair
        self.array[r][c] = v


b = B()
b[3, 3] = 100
print(b.array)
