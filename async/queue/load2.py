#!/usr/bin/env python3


import asyncio
import time

import aiohttp


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            ret = await resp.json()
    if "done" in ret:
        print(time.time(), ret["v"])
        return
    else:
        key = ret["key"]
        v = ret["v"]
        await asyncio.gather(*[
            get(f"http://localhost:9100?prm={key}-{v_}")
            for v_ in v
        ])


url = "http://localhost:9100"
asyncio.run(get(url))
