def f():
    locals()["x"] = 1
    print(x)  # これはうまく動かない


f()
