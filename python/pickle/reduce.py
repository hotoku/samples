"""
pickleの挙動をカスタマイズするには__reduce__を定義する。
cf: https://stackoverflow.com/questions/19855156/whats-the-exact-usage-of-reduce-in-pickler
"""

import pickle


class MyClass:
    def __init__(self, fpath):
        self.file = open(fpath, "w")


obj1 = MyClass("/tmp/hoge")
# pickle.dumps(obj1) => fileオブジェクトをpickleできないのでerror


class MyClass2:
    def __init__(self, fpath):
        self.fpath = fpath
        self.file = open(fpath, "w")

    def __reduce__(self):
        """
        クラスオブジェクトと、__init__への引数を渡す
        """
        return (self.__class__, (self.fpath,))


obj2 = MyClass2("/tmp/hoge2")
pickle.dumps(obj2)
