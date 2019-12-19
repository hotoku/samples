import logging


logging.basicConfig(level=logging.DEBUG)

logging.debug("debug")
logging.warning("warn")
logging.info("info")


logging.basicConfig(level=logging.WARN)  # 全部出る

logging.debug("debug 2")
logging.warning("warn 2")
logging.info("info 2")


logging.basicConfig(level=logging.INFO)  # 全部出る

logging.debug("debug 3")
logging.warning("warn 3")
logging.info("info 3")

# 後から変えても意味ないのか・・？
