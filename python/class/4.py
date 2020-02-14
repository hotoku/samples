class A:
    dic = {}
    dic2 = {}

    def __init__(self):
        self.dic2 = {}


a1 = A()
a2 = A()

a1.dic[1] = 1
a1.dic2[1] = 1
print(a2.dic)
print(a2.dic2)

# self.dicを保存しないと、変数は同一クラスのオブジェクト間で共有される
