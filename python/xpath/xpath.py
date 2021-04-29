#!/usr/bin/env python
import logging
import click
from lxml import html
LOGGER = logging.getLogger(__file__)


def doit(fp):
    xpath = '//div[contains(@class, "a-fixed-left-grid-col")]/div[contains(@class, "a-row")]/a'
    with open(fp) as f:
        dat = "".join(f.readlines())
    h = html.fromstring(dat)
    ret = h.xpath(xpath)
    for e in ret:
        print(e.text)


@click.command()
def main():
    doit("注文履歴.html")


if __name__ == "__main__":
    main()
