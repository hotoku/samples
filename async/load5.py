#!/usr/bin/env python3

import time
import asyncio
import aiohttp


def get_url(k=None, v=None):
    ret = "http://localhost:9100/"
    if k is not None:
        ret += f"?prm={k}-{v}"
    return ret


async def worker(name, queue):
    while True:
        url = await queue.get()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    ret = await resp.json()
            if "done" in ret:
                print(time.time(), ret["v"])
            else:
                key = ret["key"]
                v = ret["v"]
                for v_ in v:
                    queue.put_nowait(get_url(key, v_))
        except Exception:
            pass
        finally:
            queue.task_done()


async def main():
    queue = asyncio.Queue()
    url = get_url()
    queue.put_nowait(url)
    tasks = []
    for i in range(10):
        task = asyncio.create_task(worker(f"worker-{i}", queue))
        tasks.append(task)
    await queue.join()

    for t in tasks:
        t.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)

asyncio.run(main())
