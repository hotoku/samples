from __future__ import annotations

from abc import ABC, abstractmethod
from attr import dataclass
from datetime import date, timedelta


class Incrementable(ABC):
    @abstractmethod
    def __add__(self, n: int):
        return NotImplemented


@dataclass
class MyInt(Incrementable):
    n: int

    def __add__(self, n: int) -> MyInt:
        return MyInt(self.n + n)


@dataclass
class MyDate(Incrementable):
    d: date

    def __add__(self, n: int) -> MyDate:
        return MyDate(self.d + timedelta(days=n))
