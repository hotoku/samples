"""
luigi.cfgとlogconf.cfgの例。

1. luigi.cfgにlogconf.cfgへのパスを指定
2. logconf.cfgにログに関する設定を記述

すると、luigiのライブラリから出てくるロガーは制御できる。
一方で、アプリケーションが扱うロガーはうまくコントロールできていない。
"""

import logging
import sys
import os
import threading

import luigi

NUM_WORKER = 3


class ChildTask(luigi.Task):
    num = luigi.Parameter()

    def run(self):
        log = logging.getLogger()
        print("info about root: ", log.name, log.parent, log.level)

        log2 = logging.getLogger("luigi-interface")
        print("info about luigi-interface: ",
              log2.name, log2.parent, log2.level)

        log.error("error: %s, name=%s, pid=%d, thread=%s, loglevel=%d", self.num,
                  __name__, os.getpid(), threading.current_thread().name, log.level)
        log.warning("warning: %s, name=%s, pid=%d, thread=%s, loglevel=%d", self.num,
                    __name__, os.getpid(), threading.current_thread().name, log.level)
        log.info("info: %s, name=%s, pid=%d, thread=%s, loglevel=%d", self.num,
                 __name__, os.getpid(), threading.current_thread().name, log.level)
        log.debug("debug: %s, name=%s, pid=%d, thread=%s, loglevel=%d", self.num,
                  __name__, os.getpid(), threading.current_thread().name, log.level)

        log2.error("error: %s, name=%s, pid=%d, thread=%s, loglevel=%d", self.num,
                   __name__, os.getpid(), threading.current_thread().name, log2.level)
        log2.warning("warning: %s, name=%s, pid=%d, thread=%s, loglevel=%d", self.num,
                     __name__, os.getpid(), threading.current_thread().name, log2.level)
        log2.info("info: %s, name=%s, pid=%d, thread=%s, loglevel=%d", self.num,
                  __name__, os.getpid(), threading.current_thread().name, log2.level)
        log2.debug("debug: %s, name=%s, pid=%d, thread=%s, loglevel=%d", self.num,
                   __name__, os.getpid(), threading.current_thread().name, log2.level)

    def complete(self):
        return False


def main():
    debug = False
    if len(sys.argv) > 1 and sys.argv[1] == "-d":
        print("this is debug mode")
        debug = True

    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(levelname)s: %(asctime)s - %(name)s - %(message)s - (pid: %(process)d) - %(threadName)s"
    )

    logging.debug("debug from main")

    luigi.build(
        [ChildTask(str(n)) for n in range(3)],
        local_scheduler=True,
        workers=NUM_WORKER
    )


if __name__ == "__main__":
    main()
