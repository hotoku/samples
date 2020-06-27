#!/usr/bin/env python

"""
$ python 1.py
> Hello World!

$ pytnon 1.py -n horikoshi
> Hello horikoshi!
"""

import click


@click.command()
@click.option("--name", "-n", default="World")
def cmd(name):
    click.echo(f"Hello {name}!")


def main():
    cmd()


if __name__ == "__main__":
    main()
