from typing import AsyncIterator, Callable, Coroutine, ParamSpec, TypeVar
import asyncio

P = ParamSpec("P")
R = TypeVar("R")


def acache(f: Callable[P, Coroutine[None, None, R]]) -> Callable[P, Coroutine[None, None, R]]:
    async def ret(*args: P.args, **kwargs: P.kwargs) -> R:
        val = await f(*args, **kwargs)
        return val
    return ret


async def f(n: int) -> int:
    print("f!")
    await asyncio.sleep(1)
    return n + 100


ret = asyncio.run(f(1))
print(ret)


# これは、ちゃんと型エラーになる
# ret2 = asyncio.run(f("1"))
