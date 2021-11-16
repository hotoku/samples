from typing import Type


def get_type() -> type:
    return type("mytype", (object,), {})


x = get_type()
