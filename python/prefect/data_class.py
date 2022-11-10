"""これはうまくいかない。
dataclassの定義を別ファイルにしてimportすると動く"""

import os
from glob import glob
from dataclasses import dataclass

from prefect import flow, task


@dataclass
class File:
    folder: str
    name: str


@task
def cat_file(f: File):
    fpath = os.path.join(f.folder, f.name)
    with open(fpath) as fp:
        print(fp.read())


@task
def list_files(d: str) -> list[str]:
    return glob(f"{d}/*")


@flow
def myflow():
    ret = list_files(".")
    print(ret)


if __name__ == "__main__":
    myflow()
