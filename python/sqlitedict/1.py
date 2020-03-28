from sqlitedict import SqliteDict
import numpy as np
import time


dic = SqliteDict("./db.sqlite", autocommit=True)

start = time.time()
for i in range(10 ** 3):
    url = f"http://hogehoge.com/index?page={i}"
    dic[url] = {
        "name": f"number {i}",
        "value": np.random.random()
    }
t1 = time.time()
print("insert end", t1 - start)

for i in range(1000):
    url = f"http://hogehoge.com/index?page={i}"
    tf = url in dic

print("check end", time.time() - t1)
