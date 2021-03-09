import click
import asyncio
import time


def mysleep(n, name):
    print(f"{name} start")
    time.sleep(n)
    print(f"{name} end")


async def worker(queue):
    loop = asyncio.get_event_loop()
    while True:
        try:
            n, name = await queue.get()
            await asyncio.to_thread(mysleep, n, name)
            # await loop.run_in_executor(mysleep, n, name)
        except Exception as e:
            raise e
        finally:
            queue.task_done()


async def main():
    queue = asyncio.Queue()
    for i in range(10):
        queue.put_nowait((2, i))
    tasks = [
        asyncio.create_task(worker(queue))
        for _ in range(3)
    ]
    await queue.join()
    for t in tasks:
        t.cancel()
    asyncio.gather(*tasks, return_exceptions=True)


asyncio.run(main())
