class Hoge:
    def __getitem__(self, x):
        return x + 1


h = Hoge()
print(h[10])
# => 11


class Fuga:
    def __getitem__(self, pair):
        return pair[0] + pair[1] + 1


f = Fuga()
print(f[10, 20])
# => 31

print(f[10, :])
# => TypeError: unsupported operand type(s) for +: 'int' and 'slice'
# 文法エラーじゃない！
