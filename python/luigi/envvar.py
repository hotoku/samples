"""
環境変数は子プロセスに引き継がれる
"""

import os

import luigi


class MyTask(luigi.Task):
    num = luigi.Parameter()

    def run(self):
        val = os.getenv("LUIGI_SAMPLE")
        print(f"{self.num=}: {val=}")

    def complete(self):
        return False

    def requires(self):
        return []


def main():
    os.putenv("LUIGI_SAMPLE", "HOGE")
    tasks = [MyTask(n) for n in range(3)]

    luigi.build(
        tasks,
        workers=3,
        local_scheduler=True
    )


if __name__ == "__main__":
    main()
