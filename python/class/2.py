
class A:
    a1 = 1

    def __init__(self):
        pass


x1 = A()
print(A.a1)
print(x1.a1)
x1.a1 = 2
print(A.a1)
print(x1.a1)
