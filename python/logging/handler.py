import logging
import sys
import re

LOGGER = logging.getLogger(__file__)

_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

_to_stderr = logging.StreamHandler(sys.stderr)
_to_file = logging.FileHandler(re.sub(".py$", ".log", __file__))
_to_stderr.setFormatter(_formatter)
_to_file.setFormatter(_formatter)

LOGGER.addHandler(_to_stderr)
LOGGER.addHandler(_to_file)

LOGGER.setLevel(logging.INFO)
_to_stderr.setLevel(logging.WARNING)
_to_file.setLevel(logging.INFO)


LOGGER.debug("debug")
LOGGER.info("info")
LOGGER.warning("warn")
LOGGER.error("error")


# logのレベル判定は、LoggerとHandlerの両方で行われる
# 最初にLogger→次にHandler
# したがって、LoggerのlevelもINFOに下げておかないと、HandlerでINFOに下げてても、Loggerに弾かれる
