#!/usr/bin/env python

import argparse
import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor


"""
こうやって書いたとしても、並行処理にはならず、
start 0
end 0
start 1
end 1
...
とログに出力される。
よく考えたら、start {i}とenc {i}の間にawaitがないから、そうなるに決まっている。
"""

S = "0" * 1000000000
EX = ThreadPoolExecutor(max_workers=4)


def write(i):
    logging.info(f"start {i}")
    with open(f"11/{i}.txt", "w") as f:
        f.write(S)
    logging.info(f"end {i}")


async def in_thread(func, *args):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(EX, func, *args)


async def main():
    await asyncio.gather(*[
        in_thread(write, i) for i in range(10)
    ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    logging.basicConfig(
        filename="12.log",
        level=logging.DEBUG,
        format="[%(levelname)s]%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    asyncio.run(main())
