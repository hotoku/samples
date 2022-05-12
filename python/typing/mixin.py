from __future__ import annotations

from abc import ABC, abstractmethod
from attr import dataclass
from datetime import date, timedelta


class Incrementable(ABC):
    @abstractmethod
    def __add__(self, n: int) -> Incrementable:
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


x = MyInt(1)
z = x + 1
reveal_type(z)

# cf: https://stackoverflow.com/questions/72200332/how-can-i-declare-that-the-return-type-of-a-member-method-is-that-of-self?noredirect=1#comment127566272_72200332
