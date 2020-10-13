#!/usr/bin/env python

from glob import glob
import json
import asyncio
import aiohttp
import os
import pandas as pd
import time


def _key():
    return open("key.txt").readline().strip()


KEY = _key()
URL = "https://maps.googleapis.com/maps/api/geocode/json"
DIR = "jalan/data"


async def get(session, f, sem):
    with open(f) as f2:
        obj = json.load(f2)
    a1 = obj["address"]
    a2 = " ".join(a1.split(" ")[1:])
    print(f, "start")
    await sem.acquire()
    async with session.get(URL, params=dict(
            key=KEY,
            address=a2)) as resp:
        ret = await resp.json()
        sem.release()
        print(f, "end")
    try:
        ret2 = ret["results"][0]["geometry"]["location"]
        obj = dict(obj, **ret2)
    except IndexError:
        obj["lat"] = None
        obj["lng"] = None
    obj["geocoding"] = ret
    return obj


async def main():
    key = _key()
    sem = asyncio.Semaphore(10)
    async with aiohttp.ClientSession() as session:
        tasks = [
            get(session, f, sem) for
            f in glob(f"./{DIR}/spt_*")
        ]
        ret = await asyncio.gather(*tasks)
    keys = ret[0].keys()
    pd.DataFrame({
        k: [ret[i][k] for i in range(len(ret))]
        for k in keys
    }).to_csv("list.csv")


if __name__ == "__main__":
    asyncio.run(main())
