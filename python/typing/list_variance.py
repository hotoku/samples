from typing import List


class X:
    pass


class Y(X):
    pass


class Z(Y):
    pass


lx: List[X] = []
ly: List[Y] = []
lz: List[Z] = []

x = X()
y = Y()
z = Z()

ly.append(x)  # type erro
ly.append(z)  # type ok

ly = lx  # type error
ly = lz  # type error

x: X = ly[-1]  # type ok
z: Z = ly[-1]  # type error
