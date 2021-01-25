#!/usr/bin/env python3


# これはうまく行かない例

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
        for v_ in v:
            asyncio.create_task(get(f"http://localhost:9100?prm={key}-{v_}"))


url = "http://localhost:9100"
loop = asyncio.get_event_loop()
loop.run_until_complete(get(url))
