from threading import Semaphore
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

FILE = "temp.txt"


with open(FILE, "w") as f:
    f.write("")


def doit(i):
    with open(FILE, "a") as f:
        for j in range(100):
            f.write(f"{i},")
            time.sleep(0.01)
        f.write("\n")

with ThreadPoolExecutor(max_workers=100) as ex:
    fs = {ex.submit(doit, i): i for i in range(200)}


# ファイルの書き込みはセマフォでガードしなくても大丈夫・・・？
