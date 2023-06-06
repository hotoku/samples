from abc import ABC, abstractmethod


class AValue:
    pass


class BValue(AValue):
    pass


class CValue(BValue):
    pass


class Base(ABC):
    @abstractmethod
    def method(self, v: BValue) -> BValue:
        return NotImplemented


class Child(Base):
    # これは型エラー
    def method(self, v: CValue) -> BValue:
        return BValue()


class Child2(Base):
    # これは型エラー
    def method(self, v: BValue) -> AValue:
        return AValue()


c = Child()
