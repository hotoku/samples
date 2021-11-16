from typing import Tuple


def f(x: Tuple[int]) -> None:
    pass


y = [1, 2, 3]
f(tuple(y))

f((1, 2, 3))
