class Parent(Exception):
    pass


class Child(Parent):
    pass


try:
    raise Child()
except Parent as e:
    print(f"catch {e}")
