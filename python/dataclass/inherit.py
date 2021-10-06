from dataclasses import dataclass


@dataclass(frozen=True)
class Parent:
    x: str


@dataclass(frozen=True)
class Child(Parent):
    y: int


c = Child("a", 1)
print(c)
