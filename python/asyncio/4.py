import asyncio
from datetime import datetime

"""
for文の中にいれると並列実行されなくなる
"""


async def f(i):
    print(f"begin {i}")
    await asyncio.sleep(1)
    print(f"end {i}")


async def main():
    print(datetime.now())
    for i in range(3):
        task = asyncio.create_task(f(i))
        await task
    print(datetime.now())

asyncio.run(main())
