import numpy as np
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm


def make_closure(x, y):
    def ret():
        return x + y
    return ret


def do_one(n):
    tasks = []
    for i in range(n):
        tasks.append(make_closure(*np.random.normal(size=2)))
    values = [
        task() for task in tqdm(tasks)
    ]
    return sum(values)


def main():
    num_task = 1 * 10 ** 5
    num_process = 400

    with ProcessPoolExecutor() as ex:
        [
            ex.submit(do_one, num_task)
            for _n in range(num_process)
        ]


main()
