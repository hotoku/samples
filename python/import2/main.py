import mylib
# これはダメ
# ImportError: attempted relative import with no known parent package
# from .c import x

print(mylib.a.x)
print(mylib.x)
