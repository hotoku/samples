import pickle


def f():
    g()


def g():
    h()


def h():
    i()


def i():
    raise Exception("!")


try:
    f()
except Exception as e:
    pcl = pickle.dumps(e)

e = pickle.loads(pcl)

print(dir(e))
