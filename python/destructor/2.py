class A:
    def __del__(self):
        print("__del__")


a = A()
while True:
    print(1)
