import aiohttp
import asyncio
import time

"""
gatherで並列実行する
"""


async def fetch_one(session, id):
    print(f"id={id} start")
    url = f"https://dummy.restapiexample.com/api/v1/employee/{id}"
    ret = await session.get(url)
    print(f"id={id} end")
    return ret


async def fetch(session):
    ids = range(1, 10)
    tasks = [
        fetch_one(session, id)
        for id in ids
    ]
    ret = await asyncio.gather(*tasks)
    return ret


async def main():
    async with aiohttp.ClientSession() as session:
        ret = await fetch(session)
    print(ret)


start = time.time()
asyncio.run(main())
print(time.time() - start)
