def deco(f):
    print("decorating function")

    def ret(*args, **kwargs):
        return f(*args, **kwargs)
    return ret


print("before f is defined")


@deco
def f():
    return "f"


print("after f is defined")

print(f())
print(f())


print("before g is defined")


@deco
def g():
    return "g"


print("after g is defined")


print(g())
print(g())
