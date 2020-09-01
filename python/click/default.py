import click


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    if ctx.invoked_subcommand is None:
        hide()


@main.command()
def hello():
    print("hello")


@main.command()
def hide():
    print("hide")


main()
