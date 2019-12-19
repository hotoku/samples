def deco(f):
    def ret(*args, **kwargs):
        print("start")
        f(*args, **kwargs)
        print("end")
    return ret


@deco
def myprint(x):
    print(x)


def f(x):
    print(x)


mprint2 = deco(f)

myprint("abc")
mprint2("abc")
