"""
WARNING:root:root warning
ERROR:root:root error
INFO:9.py:info
WARNING:9.py:warning
ERROR:9.py:error

rootは、warning以上しか出ない.
9.pyは、info以上が出る.
"""

import logging


logging.debug("root debug")
logging.info("root info")
logging.warning("root warning")
logging.error("root error")

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
