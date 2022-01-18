class Hoge:
    def __init__(self):
        x = 100

    @property
    def x(self):
        return 200


hoge = Hoge()
print(hoge.x)
