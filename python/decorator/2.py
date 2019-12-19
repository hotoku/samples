def decorater_builder(val):
    def decorator(f):
        def function(*args, **kwargs):
            ret = f(*args, **kwargs) + val
            return ret
        return function
    return decorator


@decorater_builder("abc")
def makestring(x):
    return str(x)


print(makestring(111))
