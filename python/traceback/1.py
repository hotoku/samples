import traceback


def f():
    g()


def g():
    h()


def h():
    i()


def i():
    j()


def j():
    raise Exception("hoge")


try:
    f()
except Exception as e:
    print(traceback.format_exc())
