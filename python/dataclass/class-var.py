from dataclasses import dataclass


@dataclass
class Hoge:
    x: int
    y = 10


h = Hoge(1)
print(h, h.y)
# => Hoge(x=1) 10
