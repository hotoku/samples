#!/usr/bin/env python

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
def call_api(url: str) -> dict[str, Any]:
    res = requests.get(url)
    print(res. status_code)
    ret = res.json()
    return ret


@task
def parse_fact(response: dict[str, Any]) -> dict[str, Any]:
    fact = response["fact"]
    print(fact)
    return fact


@flow
def api_flow(url: str):
    fact_json = call_api(url)
    fact_text = parse_fact(fact_json)
    return fact_text


@click.command()
def main():
    ret = api_flow("https://catfact.ninja/fact")
    print(ret)


if __name__ == "__main__":
    main()
