import asyncio

"""
mainの中でawaitしないと、即座にmainが終了し、タスクもkillされる
"""

async def f(i):
    await asyncio.sleep(2)
    with open("15.txt", "a") as f:
        f.writelines([f"{i}\n"])

async def main():
    asyncio.create_task(f(1))

asyncio.run(main())
