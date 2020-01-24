#!/usr/bin/env python


"""
aiohttpを使う場合のサンプル
"""


import argparse
import asyncio
import aiohttp


class App:
    def __init__(self):
        self._session = aiohttp.ClientSession()

    async def run(self):
        pass


class SubApp(App):
    def __init__(self):
        pass


if __name__ == "__main__":
    asyncio.run(App.run())
