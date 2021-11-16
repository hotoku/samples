from typing import Generic, TypeVar, overload


@overload
def func(x: int) -> str:
    ...


@overload
def func(x: str) -> str:
    ...


def func(x):
    return str(x)


T = TypeVar("T", int, str)


class A(Generic[T]):
    def __init__(self, x: T) -> None:
        self.x = x

    def method(self) -> str:
        return func(self.x)  # pyrightではエラー
