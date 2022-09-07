import logging
import logging.config


ROOT = logging.getLogger("root")
LOGGER = logging.getLogger("simpleExample")
logging.config.fileConfig("file_config.conf")


ROOT.debug("root debug")
ROOT.info("root info")
ROOT.warning("root warning")
ROOT.error("root error")


LOGGER.debug("debug")
LOGGER.info("info")
LOGGER.warning("warning")
LOGGER.error("error")
