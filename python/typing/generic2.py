"""
overload関数の呼び出し時に型引数で指定された変数の型チェックがうまく行かない例。うまくいく例は、generic3.py

この辺の文書を参照。
https://stackoverflow.com/questions/71203939/giving-union-of-types-as-bound-argument-of-typevar-and-calling-overloaded-func/71210774#71210774
https://www.python.org/dev/peps/pep-0484/#type-variables-with-an-upper-bound
https://docs.python.org/3/library/typing.html#typing.TypeVar
"""

from typing import TypeVar, Union, overload


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


T = TypeVar("T", bound=Union[X, Y])


def func(a: T) -> T:
    f(a)
    return a
