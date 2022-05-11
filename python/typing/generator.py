from typing import Generator
import math

# Generatorの型引数は、Yield, Send, Returnの値
# 普通はYield以外はNoneでよし


def gen(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i


for i in gen(10):
    print(i)
