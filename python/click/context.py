#!/usr/bin/env python

import click
import logging


@click.group()
@click.argument("g1")
@click.pass_context
def main(ctx, g1):
    ctx.obj = dict(g1=g1)


@main.command()
@click.argument("s1")
@click.pass_obj
def sub(obj, s1):
    print(obj)
    print(s1)

if __name__ == "__main__":
    main()

# =>
# {'g1': 'a'}
# b
