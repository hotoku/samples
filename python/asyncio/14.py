#!/usr/bin/env python

import argparse
import asyncio
import logging
from aiofile import AIOFile

"""
ファイルの読み書きをawaitしたい時にはAIOFileを使う。
しかし、結局、実行時間は11.pyとほとんど変わらない。
"""


S = "0" * 1000000000


async def write(i):
    logging.info(f"start {i}")
    async with AIOFile(f"11/{i}.txt", "w") as afp:
        logging.info(f"opened {i}")
        await afp.write(S)
        logging.info(f"written {i}")
        await afp.fsync()
        logging.info(f"synced {i}")
    logging.info(f"end {i}")


async def main():
    await asyncio.gather(*[
        write(i) for i in range(10)
    ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    logging.basicConfig(
        filename="14.log",
        level=logging.DEBUG,
        format="[%(levelname)s]%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    asyncio.run(main())
