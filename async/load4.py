#!/usr/bin/env python3


import asyncio
import time
import logging

import aiohttp


logging.getLogger().setLevel(logging.INFO)


class RunningTasks:
    DIC = {}

    def __init__(self, url):
        self.url = url

    def __enter__(self):
        RunningTasks.DIC[self.url] = 1

    def __exit__(self, ex_type, ex_value, trace):
        del RunningTasks.DIC[self.url]


async def get(url):
    with RunningTasks(url):
        logging.info(f"{url} start")
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


async def main():
    url = "http://localhost:9100"
    asyncio.create_task(get(url))
    # await get(url)
    while True:
        await asyncio.sleep(0.5)
        logging.info(f"checking: {len(RunningTasks.DIC)}")
        if len(RunningTasks.DIC) == 0:
            break

asyncio.run(main())
