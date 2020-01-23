import asyncio


async def f(i):
    print(f"{i} start")
    await asyncio.sleep(3)
    print(f"{i} end")
    return i


async def main():
    f1 = f(1)
    f2 = f(2)
    f3 = f(3)
    ret = await asyncio.gather(f1, f2, f3)
    print(f"main {ret}")


asyncio.run(main())
