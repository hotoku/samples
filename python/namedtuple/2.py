from collections import namedtuple

RetAndExe = namedtuple("RetAndExe", ["value", "executed"])

re = RetAndExe(1, True)
print(re.value)
print(re.executed)
