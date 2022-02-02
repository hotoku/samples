import asyncio


async def aconnect():
    print("aconnect")
    await asyncio.sleep(1)
    return Connection()


class Connection:
    def __init__(self) -> None:
        self.vals = dict(
            America="1",
            Africa="2"
        )

    async def get(self, k):
        print("Connection.get")
        await asyncio.sleep(1)
        return self.vals[k]


class OneAtTime:
    def __init__(self, con, keys) -> None:
        self.con = con
        self.keys = keys

    def __aiter__(self):
        self.ikeys = iter(self.keys)
        return self

    async def __anext__(self):
        try:
            k = next(self.ikeys)
        except StopIteration:
            raise StopAsyncIteration

        value = await self.con.get(k)
        return value


async def process(v):
    print("process")
    await asyncio.sleep(1)
    print(v)


async def main():
    con = await aconnect()
    keys = ["America", "Africa"]

    async for v in OneAtTime(con, keys):
        await process(v)

asyncio.run(main())
