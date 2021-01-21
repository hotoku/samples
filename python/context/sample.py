class MyManager:

    def __init__(self, name="NONAME"):
        self.name = name

    def __enter__(self):
        print(f"enter: {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"exit: {self.name}")
        print(exc_type, exc_val, exc_tb)


with MyManager(1):
    print("hello")

with MyManager(2) as f:
    print("my name is", f.name)

with MyManager(3):
    print("hello")
    raise Exception("sample exception")
