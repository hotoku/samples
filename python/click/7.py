#!/usr/bin/env python

"""
オプションを必須にもできる
"""


import click


@click.command()
@click.option("--xxx", required=True)
def main(xxx):
    print(xxx)


if __name__ == "__main__":
    main()
