import time
import argparse
import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor


def f():
    time.sleep(3)
    return "f"


def g():
    time.sleep(3)
    return "g"


EX = ThreadPoolExecutor(max_workers=2)


async def in_thread(func):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(EX, func)


async def main():
    _t = time.time()
    ret = await asyncio.gather(
        in_thread(f),
        in_thread(g)
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
