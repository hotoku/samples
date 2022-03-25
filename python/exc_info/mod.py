import sys


class X:
    def __init__(self):
        print("init")

    def __del__(self):
        # __del__は、例外がプロセスによって捕捉されたあとに呼ばれるので、ここではexc_infoは見えない
        print(sys.exc_info())
        print("del")


_x = X()
