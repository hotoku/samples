import asyncio
from datetime import datetime
import time

"""
asyncのついてない関数をawaitableにする為に、run_in_executorが使える
"""


def f(i):
    time.sleep(1)
    print(i)


async def main():
    print(datetime.now())
    loop = asyncio.get_event_loop()
    f1 = loop.run_in_executor(None, f, 1)
    f2 = loop.run_in_executor(None, f, 2)
    f3 = loop.run_in_executor(None, f, 3)
    await f1
    await f2
    await f3
    print(datetime.now())

asyncio.run(main())
