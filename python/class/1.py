class A:
    a1 = 1

    def __init__(self):
        pass


x1 = A()
x2 = A()
print(x1.a1)
print(x2.a1)
x1.a1 = 2
print(x1.a1)
print(x2.a1)
