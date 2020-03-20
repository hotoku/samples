class A:
    pass


class B(A):
    pass


b = B()
print(b.__class__)
print(b is B)  # F
print(b is A)  # F
print(b.__class__ is B)  # T
print(b.__class__ is A)  # F
print(b.__class__ == B)  # T
print(b.__class__ == A)  # F
print(isinstance(b, A))  # T
