# Dictの値側は、invariantという例

from typing import Dict


class X:
    pass


class Y(X):
    pass


x: Dict[str, X] = {}
y: Dict[str, Y] = {}

x = y  # 型エラー
