#!/usr/bin/env python

import click


@click.command()
@click.argument("name")
def cmd(name):
    click.echo(f"Hello {name}!")


def main():
    cmd()


if __name__ == "__main__":
    main()
