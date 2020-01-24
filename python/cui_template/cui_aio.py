#!/usr/bin/env python


"""
CUI用のコマンド・スクリプトを作成するときのテンプレート的なサンプルasyncioを使う場合。
ログの吐き出し方がまだ分かってない。
"""


import argparse
import asyncio


class SubCommand:
    """
    Parent class of subcommands.
    The doc string of each subcommand class will appear in help message.
    The instance variable 'name' is used as the name of subcommand.
    """
    name = "This subcommand is missing a Name"

    def __init__(self, subparsers):
        self._parser = subparsers.add_parser(self.name,
                                             help=self.__doc__)
        self._register_argument(self._parser)
        self._parser.set_defaults(handler=self._handler)

    def _register_argument(self, parser):
        raise Exception(
            f"{type(self).__name__}._register_argument is not implemented.")

    async def _handler(self, args):
        raise Exception(
            f"{type(self).__name__}._handler is not implemented.")


class Greet(SubCommand):
    """
    greet
    """
    name = "greet"

    def _register_argument(self, parser):
        parser.add_argument("-n", "--num", metavar="NUM",
                            help="number of tasks",
                            default=3)

    async def greet(self):
        print("Hello ")
        await asyncio.sleep(2)
        print("world")

    async def _handler(self, args):
        await asyncio.gather(*[
            self.greet() for i in range(args.num)
        ])
        print()


class SubCommandMissing(Exception):
    pass


class App:
    """
    sample cui application
    """

    def __init__(self, args):
        self._args = args

    async def run(self):
        if hasattr(self._args, "handler"):
            await self._args.handler(self._args)
        else:
            raise SubCommandMissing("subcommand is missing")


class Setupper:
    subcommands = [
        Greet
    ]

    def __init__(self):
        self._parser = self._setup_parser()
        self.args = self._parser.parse_args()

    def _setup_parser(self):
        parser = argparse.ArgumentParser(
            description=self.__doc__)
        parser.add_argument("-l", "--log", metavar="LOG_FILE",
                            default="cui_template.log",
                            help="log file")
        parser.add_argument("-d", "--debug", action="store_true",
                            default=False,
                            help="debug mode (output debug log)")
        subparsers = parser.add_subparsers()
        for sc in Setupper.subcommands:
            sc(subparsers)
        return parser

    def print_help(self):
        self._parser.print_help()


if __name__ == "__main__":
    setup = Setupper()
    try:
        asyncio.run(App(setup.args).run())
    except SubCommandMissing as e:
        print(e)
        print()
        setup.print_help()
