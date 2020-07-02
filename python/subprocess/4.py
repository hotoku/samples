import subprocess
from io import StringIO

sin = StringIO("""hoge
fuga
""")

po = subprocess.Popen("cat", stdin=subprocess.PIPE, text=True)
po.communicate(input=sin.read())

print(po.pid)
