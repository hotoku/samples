import importlib


def doit():
    mod = importlib.import_module(".func", __name__)
    mod.hello()
