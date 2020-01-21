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
