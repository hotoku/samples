import click

"""
オプションが与えられなかった時はNoneが代入される
"""


@click.command()
@click.option("--a")
def main(a):
    print(a)


main()
