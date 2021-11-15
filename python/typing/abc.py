
from abc import ABC, abstractmethod
from typing import Union
from typing_extensions import Literal


class MyAbstract(ABC):
    @abstractmethod
    def method(self, x: Union[int, str]) -> str:
        return NotImplemented


class MyConcrete(MyAbstract):
    def method(self, x: int) -> str:  # type error. これは想定どおり
        return str(x)


class MyConcrete2(MyAbstract):
    def method(self, x: Union[int, str, float]) -> str:  # これはtype ok
        return str(x)


class MyConcrete3(MyAbstract):
    def method(self, x: Union[int, str]) -> Union[str, int]:  # type error
        return str(x)


class MyConcrete4(MyAbstract):
    def method(self, x: Union[int, str]) -> Literal["a"]:  # type ok
        return "a"


"""
mypyはデフォルトで上記のように動作するが、pyrightはデフォルトでは全てスルーしてしまう。
reportIncompatibleMethodOverrideという設定項目があるので、それを有効にする。

https://github.com/microsoft/pyright/blob/main/docs/configuration.md#sample-pyprojecttoml-file
にpyrpoject.tomlの書き方が載っている。
"""
