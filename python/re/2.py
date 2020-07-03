import re


rex = r"^ +http://localhost:([0-9]+)/\?token=([0-9a-z]+)$"
r = re.match(rex, "    http://localhost:8888/?token=815c82b388605cd0cb75527800549b5be92f25ed331313fd")
print(r.expand(r"\1"), r.expand(r"\2"))
