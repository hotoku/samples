from typing import Type


def get_type() -> Type:
    return type("mytype", (object,), {})


x = get_type()
