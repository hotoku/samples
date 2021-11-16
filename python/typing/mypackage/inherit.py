"""
mypyは見つけてくれるけど、pyrightは見つけてくれない
"""

from abc import ABC, abstractmethod


class Parent(ABC):
    @abstractmethod
    def method(self, x: int) -> int:
        return NotImplemented


class Child(Parent):
    def method(self) -> str:
        return "a"
