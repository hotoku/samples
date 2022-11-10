class MyContext:
    def __init__(self) -> None:
        pass

    def __enter__(self):
        print("enter")

    def __exit__(self, *args, **kw_args):
        print(f"exit: {args}")
        print(f"exit: {kw_args}")


try:
    with MyContext():
        pass
    with MyContext():
        raise Exception("my exception")
except Exception as e:
    print(f"catch: {e}")
