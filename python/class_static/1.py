

class Cls:
    @classmethod
    def f(cls):
        print(f"classmethod: {cls}")

    @staticmethod
    def g():
        print(f"staticmethod")


Cls.f()
Cls.g()
