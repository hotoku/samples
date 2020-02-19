from threading import Thread
import time

"""
Threadの例。クロージャーでも大丈夫。

返り値を取得することはできない・・？
https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python
"""


def f(y):
    def g(x):
        print(f"receive x={x} y={y}")
        time.sleep(2)
        return x + y
    return g


g = f(100)
threads = [
    Thread(target=g,
           args=(i,))
    for i in range(10)
]

for th in threads:
    th.start()
for th in threads:
    th.join()
