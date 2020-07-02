#!/usr/bin/env python

import argparse
import asyncio
import logging


"""
単純にファイルの読み書きをするだけではブロックしてしまう
"""

S = "0" * 1000000000


async def write(i):
    logging.info(f"start {i}")
    with open(f"11/{i}.txt", "w") as f:
        f.write(S)
    logging.info(f"end {i}")


async def main():
    await asyncio.gather(*[
        write(i) for i in range(10)
    ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    logging.basicConfig(
        filename="11.log",
        level=logging.DEBUG,
        format="[%(levelname)s]%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    asyncio.run(main())
