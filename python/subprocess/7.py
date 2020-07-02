import subprocess

"""
このファイルを起動したプロセスは、すぐに終了する。
このファイルから起動されたプロセスは、ずっと残る。
"""


po = subprocess.Popen(["python", "-c", "while True: 1"], stdin=subprocess.PIPE, text=True)
print(po.pid)
