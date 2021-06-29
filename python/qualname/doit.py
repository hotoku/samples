from sample import func, cls


def func2(x):
    print(x)


print(func.func.__module__, func.func.__qualname__)
print(func2.__module__, func2.__qualname__)

obj = cls.Cls()
print(obj.func.__module__, obj.func.__qualname__)
