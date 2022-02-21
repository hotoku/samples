from typing import TypeVar, Union


class X:
    def method(self) -> float:
        return 1.0


class Y:
    def method(self) -> float:
        return 1.0


T = TypeVar("T", bound=Union[X, Y])


def func(a: T) -> T:
    a.method()
    return a
