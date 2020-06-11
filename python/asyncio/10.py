import time
import argparse
import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor


def f(s, t):
    time.sleep(3)
    return s + t


def g(s, t):
    time.sleep(3)
    return s + t


EX = ThreadPoolExecutor(max_workers=2)


async def in_thread(func, *args):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(EX, func, *args)


async def main():
    _t = time.time()
    ret = await asyncio.gather(
        in_thread(f, 1, 2),
        in_thread(g, 1, 2)
    )
    print(ret)
    print(time.time() - _t)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    logging.basicConfig(
        filename="10.log",
        level=logging.DEBUG,
        format="[%(levelname)s]%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    asyncio.run(main())
