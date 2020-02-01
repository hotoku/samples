import asyncio
import logging


logging.basicConfig(level=logging.DEBUG)


async def f(i):
    logging.info(f"{i} start")
    await asyncio.sleep(1)
    logging.info(f"{i} end")


async def main():
    await asyncio.gather(
        f(1),
        f(2),
        f(3)
    )

asyncio.run(main())
