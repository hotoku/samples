#!/usr/bin/env python

import argparse
import logging


def main(args):
    print(args.c_d)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # これへのアクセスの仕方が分からない
    # args.a_bではダメ
    parser.add_argument("a-b")
    parser.add_argument("--c-d", default="x")
    args = parser.parse_args()

    logging.basicConfig(
        filename="5.log",
        level=logging.DEBUG,
        format="[%(levelname)s]%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    main(args)
