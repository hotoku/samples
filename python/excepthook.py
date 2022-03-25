import sys


class X:
    value = ""

    def __init__(self):
        print("init")

    def __del__(self):
        print(f"del: {self.value}")


def myhook(*args):
    print("hook")
    X.value = "updated"
    sys.__excepthook__(*args)


x = X()

sys.excepthook = myhook
raise RuntimeError()

# これだと、X.__del__が呼ばれなくなってしまった
