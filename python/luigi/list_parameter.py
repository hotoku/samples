"""
ListParameterは、パラメータのリストの順序が違えば別のタスクとみなされる。
この例では、["a", "b"]と["b", "a"]の両方のタスクが実行される。
"""

import hashlib
import datetime


import luigi


class ChildTask(luigi.Task):
    def requires(self):
        return [
            ParentTask(["a", "b"]),
            ParentTask(["b", "a"])
        ]


class ParentTask(luigi.Task):
    names = luigi.ListParameter()

    @staticmethod
    def path(names: list[str]) -> str:
        ls = sorted(names)
        s = "".join(ls)
        name = hashlib.sha256(s.encode()).hexdigest()
        return f"/tmp/hoge/{name}"

    def output(self):
        return [
            luigi.local_target.LocalTarget(self.path(self.names))
        ]

    def run(self):
        with open(self.path(self.names), "a") as fp:
            fp.write("%s, %s\n" % (datetime.datetime.now(), self.names))


luigi.build(
    [ChildTask()],
    local_scheduler=True
)
