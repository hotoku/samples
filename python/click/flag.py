import click


@click.command()
@click.option("--flag/--no-flag", default=False)
def main(flag):
    print(flag)


main()
