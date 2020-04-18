"""
subprocessで終了コード
"""


import subprocess as sp

ret = sp.run("ls")
print("ret =", ret.returncode)


ret = sp.run("false")
print("ret =", ret.returncode)
