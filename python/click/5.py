import asyncio
from functools import wraps
import click


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@click.command()
@coro
async def main():
    await asyncio.sleep(1)
    click.echo("Delayed hello")


asyncio.run(main())
