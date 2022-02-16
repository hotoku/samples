class MyEx(Exception):
    def __init__(self, t: type) -> None:
        super().__init__(f"type={t}")


raise MyEx(MyEx)
