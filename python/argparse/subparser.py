#!/usr/bin/env python

"""argparseでサブコマンドを扱う例
"""


import argparse


def cmd2(subparsers: argparse._SubParsersAction, name: str) -> None:
    parser = subparsers.add_parser(name)
    parser.add_argument("hoge", type=str)

    def run(args):
        print("cmd2", args.hoge)

    parser.set_defaults(handler=run)


def cmd1(subparsers: argparse._SubParsersAction, name: str) -> None:
    parser = subparsers.add_parser(name)
    parser.add_argument("hoge", type=str)

    def run(args):
        print("cmd1", args.hoge)

    parser.set_defaults(handler=run)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    cmd1(subparsers, "cmd1")
    cmd2(subparsers, "cmd2")

    args = parser.parse_args()
    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    main()
