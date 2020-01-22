import aiohttp
import asyncio
import time

"""
gatherで並列実行する
"""


async def fetch_one(session, id):
    print(f"id={id} start")
    url = f"https://reqres.in/api/users/{id}"
    ret = await session.get(url)
    print(f"id={id} end")
    return ret


async def main():
    async with aiohttp.ClientSession() as session:
        ret = await fetch_one(session, 1)
    body = await ret.text()
    print(f"body={body}")


asyncio.run(main())
