import re

s = "http://hoge.com/fuga/101/"
t = re.sub(r"http://hoge.com/fuga/(.+)/", r"\1", s)
print(t)
