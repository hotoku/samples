class A:
    def __getitem__(self, x):
        return 1


a = A()
print(a["a"])
