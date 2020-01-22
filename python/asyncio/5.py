import asyncio
from datetime import datetime

"""
複数のcoroutineを同時に実行するにはgatherを使う。
gatherをawaitしないと、処理がプログラム先に進んでしまい、
ファイルの最後でタスクがキャンセルされて終わる。
"""


async def f(i):
    print(f"begin {i}")
    await asyncio.sleep(1)
    print(f"end {i}")


async def main():
    print(datetime.now())
    tasks = [f(i) for i in range(3)]
    ret = await asyncio.gather(*tasks)  # awaitしないと、処理が先に進んでしまう
    print(ret)

asyncio.run(main())
