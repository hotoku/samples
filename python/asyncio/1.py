import asyncio
from datetime import datetime

"""
この書き方だと、並列実行されないので、3秒かかる
"""


async def f(i):
    await asyncio.sleep(1)
    print(i)


async def main():
    print(datetime.now())
    await f(1)
    await f(2)
    await f(3)
    print(datetime.now())

asyncio.run(main())
