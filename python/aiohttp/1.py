import aiohttp
import asyncio
import time

"""
これだと、並列に実行されない。
"""


async def fetch(session):
    ids = range(1, 10)
    ret = {}
    for id in ids:
        print(f"id={id} start")
        url = f"https://dummy.restapiexample.com/api/v1/employee/{id}"
        ret[id] = await session.get(url)
        print(f"id={id} done")

    return ret


async def main():
    async with aiohttp.ClientSession() as session:
        ret = await fetch(session)
    print(ret)


start = time.time()
asyncio.run(main())
print(time.time() - start)
