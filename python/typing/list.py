# Listの値の型は、invariantという例
# https://stackoverflow.com/questions/64481378/expected-type-lista-matched-generic-type-list-t-got-listb-instead
# > A mutable container such as List is invariant because elements can be both inserted into (contravariant) and
# > taken from (covariant) the list. If mutability is not required, using an immutable Sequence provides valid type annotation:

from typing import List


class X:
    pass


class Y(X):
    pass


x: List[X] = []
y: List[Y] = []

x = y  # 型エラー
