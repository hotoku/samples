from typing import Any, Optional

import click


class IntList(click.ParamType):
    name = "IntList"

    def convert(
        self, value: Any, param: Optional[click.Parameter], ctx: Optional[click.Context]
    ) -> list[int]:
        if isinstance(value, str):
            ss = value.split(",")
            return list(map(int, ss))
        if isinstance(value, list):
            return value
        if param is None and ctx is None:
            return []
        assert False, "panic. IntList.convert"


@click.command()
@click.argument("ls", type=IntList())
def main(ls):
    print(ls)


main()
