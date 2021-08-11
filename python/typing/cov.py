

from typing import Generic, TypeVar


T = TypeVar("T", covariant=True)


class Container(Generic[T]):
    pass


class A:
    pass


class B(A):
    pass


class C(B):
    pass


# x: Container[B] = Container[A]() # type error
x: Container[B] = Container[C]()
