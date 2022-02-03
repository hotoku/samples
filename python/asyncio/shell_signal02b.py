import asyncio
from signal import SIGINT, SIGTERM
import os


async def main():
    loop = asyncio.get_running_loop()
    for sig in (SIGTERM, SIGINT):
        loop.add_signal_handler(sig, handler, sig)

    try:
        while True:
            print(f"running: {os.getpid()}")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        for i in range(10):
            print("shutting down ...")
            await asyncio.sleep(1)


def handler(sig):
    loop = asyncio.get_running_loop()
    for task in asyncio.all_tasks(loop=loop):
        task.cancel()
    print(f"got signal: {sig}, shutting down")
    loop.remove_signal_handler(SIGTERM)
    loop.add_signal_handler(SIGINT, lambda: None)


if __name__ == "__main__":
    asyncio.run(main())
