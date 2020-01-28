def red(s):
    return color(s, 31)


def green(s):
    return color(s, 32)


def cyan(s):
    return color(s, 36)


def color(s, c):
    return f"\033[{c}m{s}\033[0m"


print(red("red"))
print(green("green"))
print(cyan("cyan"))
