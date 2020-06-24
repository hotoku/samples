from tqdm import tqdm

s = 0
for i in tqdm(range(10000000)):
    s += 1
print(s)
