class A:
    def __getattr__(self, name):
        return name


a = A()
print(a.hoge)
# print(A.hoge) # => error

A.__getattr__ = lambda self, name: name

print(A.hoge)  # => error
