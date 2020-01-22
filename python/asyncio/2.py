import asyncio
from datetime import datetime

"""
並列実行させる為には、create_taskに包む。
並列実行させれば、1秒で終わる。
"""


async def f(i):
    print(f"begin {i}")
    await asyncio.sleep(1)
    print(f"end {i}")


async def main():
    print(datetime.now())
    f1 = asyncio.create_task(f(1))
    f2 = asyncio.create_task(f(2))
    f3 = asyncio.create_task(f(3))
    await f1
    await f2
    await f3
    print(datetime.now())

asyncio.run(main())
