#!/usr/bin/env python

import click


@click.group()
def cmd():
    pass


@cmd.command()
def english():
    click.echo("Hello World!")


@cmd.command()
def japanese():
    click.echo("こんにちは 世界!")


def main():
    cmd()


if __name__ == "__main__":
    main()
