"""
overload関数の呼び出し時に型引数で指定された変数の型チェックがうまく行く例。
mypyだとOKで、pyright (1.1.223)だとNG..
"""

from typing import TypeVar, overload


class X:
    pass


class Y:
    pass


@overload
def f(a: X):
    ...


@overload
def f(a: Y):
    ...


def f(a):
    return


T = TypeVar("T", X, Y)


def func(a: T) -> T:
    f(a)
    return a
