"""
これは動作する
"""





def new(cls):
    return 1

class MyMeta(type):
    def __add__(self, other):
        return type(self.__name__ + other.__name__, (MyMeta,), {"__new__": new})

class Hoge(metaclass=MyMeta):
    pass

class Fuga(metaclass=MyMeta):
    pass

HogeFuga = Hoge + Fuga

hf = HogeFuga() 
print(hf)
