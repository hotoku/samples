#!/usr/bin/env python


import argparse
import sys

parser = argparse.ArgumentParser(description="sample")
subparsers = parser.add_subparsers()


def h_hoge(args):
    print(f"hoge: {args.all}")


def h_fuga(args):
    print(f"fuga: {args.base}")


sp_hoge = subparsers.add_parser("hoge", help="help of hoge")
sp_hoge.add_argument("-A", "--all", action="store_true")
sp_hoge.set_defaults(handler=h_hoge)

sp_fuga = subparsers.add_parser("fuga", help="help of fuga")
sp_fuga.add_argument("-B", "--base", metavar="NUM", help="some number")
sp_fuga.set_defaults(handler=h_fuga)


args = parser.parse_args()
if hasattr(args, "handler"):
    args.handler(args)
else:
    print("command is invalid or not supplied\n\n")
    parser.print_help()
