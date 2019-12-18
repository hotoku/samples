class A:
    def __init__(self):
        self.x = 1


class B(A):
    def __init__(self):
        super(B, self).__init__()


x = B()
print(x.x)
