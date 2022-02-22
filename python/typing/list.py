# Listの値の型は、invariantという例

from typing import List


class X:
    pass


class Y(X):
    pass


x: List[X] = []
y: List[Y] = []

x = y  # 型エラー
