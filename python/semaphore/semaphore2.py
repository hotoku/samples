from threading import Semaphore
from concurrent.futures import ThreadPoolExecutor
import time

FILE = "temp2.txt"


with open(FILE, "w") as f:
    f.write("")

sem = Semaphore(1)


def doit(i):
    if sem.acquire():
        with open(FILE, "a") as f:
            for j in range(10):
                if j > 0:
                    f.write(",")
                f.write(f"{i}")
                time.sleep(0.01)
            f.write("\n")
    sem.release()


with ThreadPoolExecutor(max_workers=50) as ex:
    fs = {ex.submit(doit, i): i for i in range(100)}
