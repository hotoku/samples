from abc import ABC, abstractmethod
from typing import Iterable, TypeVar


T = TypeVar("T")


class A(ABC):
    @abstractmethod
    def method(self, x: T, y: Iterable[T]) -> None:
        pass


class B(A):
    def method(self, x: T, y: T) -> None:  # これがincompatible overrideにならない・・・のはなんぜ？
        x, y
