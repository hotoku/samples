import asyncio


async def f(n, sem):
    async with sem:
        print(n)
        await asyncio.sleep(1)


async def run():
    sem = asyncio.Semaphore(2)
    # https://stackoverflow.com/questions/55918048/asyncio-semaphore-runtimeerror-task-got-future-attached-to-a-different-loop
    tasks = [f(i, sem) for i in range(6)]
    await asyncio.gather(*tasks)

asyncio.run(run())
