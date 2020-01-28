#!/usr/bin/env python

import os
import pickle


def cached(path):
    def decorator(func):
        def ret(*args, **kwargs):
            if os.path.exists(path):
                with open(path, "br") as f:
                    return pickle.load(f)
            else:
                obj = func(*args, **kwargs)
                with open(path, "bw") as f:
                    pickle.dump(obj, f)
                return obj
        return ret
    return decorator


@cached("6.pkl")
def f(n):
    print("calculating ...")
    return n


print(f(1))
print(f(1))
