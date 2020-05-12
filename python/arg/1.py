def f(*args, **kwargs):
    print(args)
    print(kwargs)


f(1, 2, 3)
f(x=1, y=2)
