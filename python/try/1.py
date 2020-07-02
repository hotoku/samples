try:
    raise Exception("a")
except Exception as e:
    print(e)
else:
    print("else")
