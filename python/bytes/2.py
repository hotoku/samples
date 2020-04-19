s = "あ"
b = s.encode("utf-8")
print(type(b), b)
s2 = b.decode("utf-8")
print(type(s2), s2)
