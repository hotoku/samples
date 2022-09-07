"""
luigiが起動するサブプロセスには、グローバル変数は引き継がれない。
このスクリプトでは、MyTask:runから出力されるMY_OBJはNone。
"""

from dataclasses import dataclass

import luigi


@dataclass
class Obj:
    x: int


MY_OBJ = None


class MyTask(luigi.Task):
    num = luigi.Parameter()

    def run(self):
        print(f"{self.num=}")
        print(f"{MY_OBJ=}")

    def complete(self):
        return False

    def requires(self):
        return []


def main():
    global MY_OBJ
    MY_OBJ = Obj(10)
    print(MY_OBJ)
    tasks = [MyTask(n) for n in range(3)]

    luigi.build(
        tasks,
        workers=3,
        local_scheduler=True
    )


if __name__ == "__main__":
    main()
