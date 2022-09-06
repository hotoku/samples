import logging

LOGGER = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s - (pid: %(process)d) - %(threadName)s"
)

LOGGER.debug("this is debug")
