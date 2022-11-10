#!/usr/bin/env python

import os
import time
import logging

import click
from prefect import flow, task
from prefect_dask import DaskTaskRunner

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s"
)


class Container:
    mylist: list[int] = []

    @classmethod
    def add(cls, n: int):
        cls.mylist.append(n)


@task
def print_values(values: list[int]):
    for i, value in enumerate(values):
        time.sleep(0.5)
        Container.add(value)
        print(i, os.getpid(), value, Container.mylist)


@flow(task_runner=DaskTaskRunner())
def my_flow():
    n = 3
    print_values.submit(list(range(n)))
    print_values.submit(list(range(100, 100 + n)))


@click.command()
def main():
    Container.add(-100)
    my_flow()


if __name__ == "__main__":
    main()

# =>
# 0 23909 0 [-100, 0]
# 1 23909 1 [-100, 0, 1]
# 2 23909 2 [-100, 0, 1, 2]
# 0 23910 100 [-100, 100]
# 1 23910 101 [-100, 100, 101]
# 2 23910 102 [-100, 100, 101, 102]
