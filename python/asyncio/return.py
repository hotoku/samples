import asyncio


async def f() -> int:
    return 1

ret = asyncio.run(f())
print(ret)
