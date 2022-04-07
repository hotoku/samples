from abc import ABC, abstractmethod


class Hoge(ABC):
    @property
    @abstractmethod
    def hoge(self) -> str:
        ...


class Fuga(Hoge):
    hoge = "fuga"


class Piyo(Hoge):
    pass


f = Fuga()  # ok
p = Piyo()  # ng
