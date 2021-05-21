import hashlib
import os
import pickle


USE_CACHE = True
CACHE_DIR = ".cache"
os.makedirs(CACHE_DIR, exist_ok=True)


def cache(ignore_pos=[], ignore_kw=[]):
    def decorator(f):
        def ret(*args, **kw):
            a2 = [a for i, a in enumerate(args) if i not in ignore_pos]
            k2 = {k: v for k, v in kw.items() if k not in ignore_kw}
            key = {
                "args": a2,
                "kw": k2
            }
            ser = pickle.dumps(key)
            hash_ = hashlib.sha256(ser).hexdigest()
            fpath = os.path.join(".cache", f"{f.__name__}_{hash_}")
            if USE_CACHE and os.path.exists(fpath):
                with open(fpath, "rb") as fp:
                    return pickle.load(fp)
            ret = f(*args, **kw)
            with open(fpath, "wb") as fp:
                pickle.dump(ret, fp)
            return ret
        return ret
    return decorator


@cache()
def f(x):
    print(f"f({x})")
    return x + 1


print(f(1))
print(f(2))
print(f(1))
