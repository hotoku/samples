"""
luigiのワーカーは、別プロセスが立ち上がる。
その際に、モジュールが改めてロードされる。
親プロセスの中で、loggingに関する設定をしていても、子プロセスにはそれは反映されない。

このスクリプトでは、mainの中でlogging.basicConfigを呼んでいるが、これはif __name__ == "__main__":で
ガードされているので、子プロセスがこのモジュールをロードした際には呼び出されない。
そのため、ChildTask:runのログは、warning以上しか表示されない。
"""

import logging
import sys
import os
import threading

import luigi

LOGGER = logging.getLogger(__name__)
NUM_WORKER = 3

print(
    f"this message will be displayed <num worker + 1> = {NUM_WORKER + 1} times.")


class ChildTask(luigi.Task):
    num = luigi.Parameter()

    def run(self):
        LOGGER.error("error: %s, name=%s, =%d, thread=%s", self.num,
                     __name__, os.getpid(), threading.current_thread().name)
        LOGGER.warning("warning: %s, name=%s, =%d, thread=%s", self.num,
                       __name__, os.getpid(), threading.current_thread().name)
        LOGGER.info("warn: %s, name=%s, =%d, thread=%s", self.num,
                    __name__, os.getpid(), threading.current_thread().name)
        LOGGER.debug("debug: %s, name=%s, =%d, thread=%s", self.num,
                     __name__, os.getpid(), threading.current_thread().name)


def main():
    debug = False
    if len(sys.argv) > 1 and sys.argv[1] == "-d":
        print("this is debug mode")
        debug = True

    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(levelname)s: %(asctime)s - %(name)s - %(message)s - (pid: %(process)d) - %(threadName)s"
    )

    LOGGER.debug("debug from main")

    luigi.build(
        [ChildTask(str(n)) for n in range(3)],
        local_scheduler=True,
        workers=NUM_WORKER
    )


if __name__ == "__main__":
    main()
