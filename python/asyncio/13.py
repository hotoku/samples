#!/usr/bin/env python

import argparse
import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor


"""
f.writeをin_threadで包んでやれば、並行にファイル出力されているように見える。
つまり、13.logに
start 0
start 1
start 2
...
end 0
end 1
end 2
...
と出力される。
しかし、start 0からstart 1までに1秒くらいかかっており、結局、並行処理されてなさそう。
"""

S = "0" * 1000000000
EX = ThreadPoolExecutor(max_workers=4)


async def write(i):
    logging.info(f"start {i}")
    with open(f"11/{i}.txt", "w") as f:
        await in_thread(lambda f: f.write(S), f)
    logging.info(f"end {i}")


async def in_thread(func, *args):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(EX, func, *args)


async def main():
    await asyncio.gather(*[
        write(i) for i in range(10)
    ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    logging.basicConfig(
        filename="13.log",
        level=logging.DEBUG,
        format="[%(levelname)s]%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    asyncio.run(main())
