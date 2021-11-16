from typing import Generic, TypeVar, Union, overload


@overload
def func(x: int) -> str:
    ...


@overload
def func(x: str) -> str:
    ...


def func(x):
    return str(x)


def func2(x: Union[int, str]) -> str:
    return str(x)


T = TypeVar("T", int, str)


class A(Generic[T]):
    def __init__(self, x: T) -> None:
        self.x = x

    def method(self) -> str:
        return func(self.x)  # pyrightではエラー

    def method2(self) -> str:
        return func2(self.x)  # これはOK


S = TypeVar("S", bound=Union[int, str])


class B(Generic[S]):
    def __init__(self, x: S) -> None:
        self.x = x

    def method(self) -> str:
        return func(self.x)  # これでもダメ

    def method2(self) -> str:
        return func2(self.x)  # これはOK
