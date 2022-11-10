#!/usr/bin/env python

import time
import logging

import click
from prefect import flow, task
from prefect_dask import DaskTaskRunner

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s"
)


@task
def print_values(values: list[str]):
    for i, value in enumerate(values):
        time.sleep(0.5)
        print(i, value, end="\r")


@flow(task_runner=DaskTaskRunner())
def my_flow():
    print_values.submit(["AAAA"] * 15)
    print_values.submit(["BBBB"] * 10)


@click.command()
def main():
    my_flow()


if __name__ == "__main__":
    main()
