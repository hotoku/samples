from typing import Callable, Any, List, TypeVar

V = TypeVar("V")


def func(f: Callable[..., V]) -> Callable[..., List[V]]:
    def make_list(*args, **kwargs):
        return args
    return make_list
