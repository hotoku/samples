from datetime import datetime

class Foo:
    pass

class MyMeta(type):
    def __add__(self, other):
        return MyMeta(self.__name__ + other.__name__, (MyMeta,), {})

class Hoge(metaclass=MyMeta):
    pass

class Fuga(metaclass=MyMeta):
    pass

h = Hoge()

HogeFuga = Hoge + Fuga

# ここでエラー
# TypeError: type.__new__() takes exactly 3 arguments (0 given)
hf = HogeFuga() 
