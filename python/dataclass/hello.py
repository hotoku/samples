from dataclasses import dataclass


@dataclass
class A:
    x: int
    y: str


a = A(10, "a")
print(a)
