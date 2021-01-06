#!/usr/bin/env python

import logging
import sys
import re
import click

LOGGER = logging.getLogger(__file__)


def setup_logger(debug):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    to_stderr = logging.StreamHandler(sys.stderr)
    to_file = logging.FileHandler(re.sub(r".py$", r".log", __file__))
    to_stderr.setFormatter(formatter)
    to_file.setFormatter(formatter)
    LOGGER.addHandler(to_stderr)
    LOGGER.addHandler(to_file)
    if debug:
        LOGGER.setLevel(logging.DEBUG)
        to_stderr.setLevel(logging.DEBUG)
        to_file.setLevel(logging.DEBUG)
    else:
        LOGGER.setLevel(logging.INFO)
        to_stderr.setLevel(logging.WARN)
        to_file.setLevel(logging.INFO)


@click.command()
@click.option("--debug/--no-debug", "-d", default=False)
def main(debug):
    setup_logger(debug)
    LOGGER.debug("debug")
    LOGGER.info("info")
    LOGGER.warning("warn")
    LOGGER.error("error")

if __name__ == "__main__":
    main()
