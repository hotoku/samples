from typing import Generic, TypeVar

"""
同じ型変数を使っていても、別の場所では別の型として解釈される。
当たり前やね
"""


Type1 = TypeVar("Type1")


class Class1(Generic[Type1]):
    def __init__(self, x: Type1) -> None:
        self.x = x


class Class2(Generic[Type1]):
    def __init__(self, x: Type1) -> None:
        self.x = x


v1 = Class1[int](1)
v2 = Class2[str]("a")
