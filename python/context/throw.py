class MyContext:
    def __init__(self) -> None:
        pass

    def __enter__(self):
        print("enter")

    def __exit__(self, exc, *_):
        print(f"exit: {exc}")


try:
    with MyContext():
        raise Exception("my exception")
except Exception as e:
    print(f"catch: {e}")
