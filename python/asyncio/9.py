"""
asyncではない関数を並列実行するには、loop.run_in_executorを使う。
https://docs.python.org/ja/3/library/asyncio-eventloop.html
"""

import asyncio
from time import sleep


def f(n):
    print(n)
    sleep(1)


async def main():
    loop = asyncio.get_event_loop()
    await asyncio.gather(*[
        loop.run_in_executor(None, f, i) for i in range(10)
    ])


asyncio.run(main())
