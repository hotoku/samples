from tempfile import NamedTemporaryFile, TemporaryFile
import shutil


class ErrorHandler:

    def __init__(self, fpath):
        self.fpath = fpath
        self.fd = None

    def __enter__(self):
        self.fd = NamedTemporaryFile(mode="w")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            return
        self.fd.flush()
        shutil.copy(self.fd.name, self.fpath)

    def write(self, l):
        self.fd.write(l)

    def writelines(self, ls):
        self.fd.writelines(ls)

with ErrorHandler("./temp.txt") as f:
    f.write("a\n")
    f.writelines([f"{i}\n" for i in range(10)])

with ErrorHandler("./temp2.txt") as f:
    f.write("b\n")
    raise Exception("error")
