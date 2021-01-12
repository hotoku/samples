import luigi


class T1(luigi.Task):
    name = luigi.Parameter()

    def requires(self):
        return []

    def output(self):
        return [
            luigi.local_target.LocalTarget(self.path())
        ]

    def path(self):
        return f"{self.name}.txt"

    def run(self):
        with open(self.path(), "w") as f:
            f.write("a")

tasks = [T1("a")]
luigi.build(
    tasks,
    local_scheduler=True,
    workers=4
)
