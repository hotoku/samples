# 参考：https://devlights.hatenablog.com/entry/2019/05/26/014741

# typeは、クラス名、親クラスのタプル、属性の辞書を引数に取る


# シンプルな例
A = type("A", (object,), {"a": 100})

a = A()
print(a.a)


# 継承させる場合
class B:

    def run(self):
        print(self.value)

C = type("C", (B,), {})


c = C()
c.value = 101
c.run()


# types.new_classを使う場合
# types.new_classには、exec_bodyを渡せる
# exec_bodyは、「新規に作成されたクラスの名前空間を構築するためのコールバック」で、
# 辞書を受け取り、辞書を返す。
# こいつの中で、関数を定義して差し込んでやれば、動的な関数の中にメソッドを作成することができる。
import types


def init_D(dic):
    def __init__(self, value):
        self.value = value

    def run2(self):
        print("start run2")
        self.run()
    dic["__init__"] = __init__
    dic["run2"] = run2
    return dic

D = types.new_class("D", (B,), exec_body=init_D)

d = D(102)
d.run()
d.run2()
