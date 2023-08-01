import asyncio


async def myiter():
    for i in range(3):
        await asyncio.sleep(1)
        yield i


async def main():
    async for i in myiter():
        print(i)

asyncio.run(main())
