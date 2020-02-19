from concurrent.futures import ProcessPoolExecutor
import time

"""
なぜか動かない例。Pickleできない！というエラーは出ない。
実行すると、画面に何も表示されず、いつまでたっても終わらない。
"""


def f(y):
    def g(x):
        print(f"receive x={x} y={y}")
        time.sleep(2)
        return x + y
    return g


g = f(100)
with ProcessPoolExecutor() as executor:
    ret = executor.map(g, range(4))

print(ret)
