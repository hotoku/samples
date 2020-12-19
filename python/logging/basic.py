#!/usr/bin/env python

"""
# loggingの使用例

標準エラーとファイルにログを出力する。

## 使い方
`./basic.py run` または `./basic.py --debug run`

`--debug`を付けない場合、`warn`以上を標準エラー出力に送り、`info`以上をログファイルに送る。
`--debug`を付けると、`debug`以上を標準エラー出力とログファイルの両方に送る。

"""

import logging
import sys
import os
import re

import click


LOGGER = logging.getLogger(__file__)


def setup_logger(debug=False):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    to_stderr = logging.StreamHandler(sys.stderr)
    to_stderr.setFormatter(formatter)
    to_file = logging.FileHandler(os.path.split(re.sub(r"\.py$", ".log", __file__))[1])
    to_file.setFormatter(formatter)
    LOGGER.addHandler(to_stderr)
    LOGGER.addHandler(to_file)
    if not debug:
        LOGGER.setLevel(logging.INFO)
        to_stderr.setLevel(logging.WARNING)
        to_file.setLevel(logging.INFO)
    else:
        LOGGER.setLevel(logging.DEBUG)
        to_stderr.setLevel(logging.DEBUG)
        to_file.setLevel(logging.DEBUG)


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.pass_context
def main(ctx, debug):
    setup_logger(debug)


@main.command()
@click.pass_context
def run(ctx):
    LOGGER.debug("debug")
    LOGGER.info("info")
    LOGGER.warning("warning")


if __name__ == "__main__":
    main()
