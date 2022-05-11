from typing import Generator
import math


def gen(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i


for i in gen(10):
    print(i)
