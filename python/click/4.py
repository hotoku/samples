#!/usr/bin/env python

"""
これはエラー
"""


import click


@click.command()
@click.argument("name")
def cmd(n):
    click.echo(f"Hello {n}!")


def main():
    cmd()


if __name__ == "__main__":
    main()
