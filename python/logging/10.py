"""
DEBUG:root:root debug
INFO:root:root info
WARNING:root:root warning
ERROR:root:root error
DEBUG:10.py:debug
INFO:10.py:info
WARNING:10.py:warning
ERROR:10.py:error

rootも10.pyもdebug以上が出る
"""

import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("root debug")
logging.info("root info")
logging.warning("root warning")
logging.error("root error")

logger = logging.getLogger(__file__)

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
