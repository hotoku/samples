from typing import TypeVar, Sequence

T = TypeVar("T", float, int)


def ensure_non_negative(xs: Sequence[T]) -> Sequence[T]:
    return [max(x, 0) for x in xs]  # これは型エラー
