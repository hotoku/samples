import time
import asyncio


def blocking():
    time.sleep(1.5)
    print(f"{time.ctime()} hello from a thread!")


async def main():
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, blocking)
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")

asyncio.run(main())
