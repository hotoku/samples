import json
from io import StringIO

sio = StringIO("""
{
  "a": "hoge"
}
""")
j = json.load(sio)

print(j)
# print(j.a) # これはエラー
print(j["a"])
