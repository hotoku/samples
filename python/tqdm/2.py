from tqdm import tqdm

cnt = tqdm(range(100))
next(cnt)  # type error. tqdm is not an iterator
