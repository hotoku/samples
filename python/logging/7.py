import logging


l1 = logging.getLogger("1")
l2 = logging.getLogger("2")


l1.setLevel(logging.DEBUG)
l2.setLevel(logging.INFO)

logging.debug("root debug")
l1.debug("l1 debug")
l2.debug("l2 debug")


logging.info("root info")
l1.info("l1 info")
l2.info("l2 info")


logging.warning("root warning")
l1.warning("l1 warning")
l2.warning("l2 warning")
