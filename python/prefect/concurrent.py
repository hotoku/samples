#!/usr/bin/env python

import time
import logging
from typing import Any

import requests
import click
from prefect import flow, task


LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s"
)


@task
def print_values(values: list[str]):
    for value in values:
        time.sleep(0.5)
        print(value, end="\r")


@flow
def my_flow():
    print_values.submit(["AAAA"] * 15)
    print_values.submit(["BBBB"] * 10)


@click.command()
def main():
    my_flow()


if __name__ == "__main__":
    main()
