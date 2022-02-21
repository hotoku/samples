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
