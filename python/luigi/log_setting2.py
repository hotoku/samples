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
        logging.error("error: %s, name=%s, =%d, thread=%s", self.num,
                      __name__, os.getpid(), threading.current_thread().name)
        logging.warning("warning: %s, name=%s, =%d, thread=%s", self.num,
                        __name__, os.getpid(), threading.current_thread().name)
        logging.info("warn: %s, name=%s, =%d, thread=%s", self.num,
                     __name__, os.getpid(), threading.current_thread().name)
        logging.debug("debug: %s, name=%s, =%d, thread=%s", self.num,
                      __name__, os.getpid(), threading.current_thread().name)

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
