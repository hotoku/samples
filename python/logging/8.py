"""
stdoutとファイル両方に
https://stackoverflow.com/questions/14058453/making-python-loggers-output-all-messages-to-stdout-in-addition-to-log-file
"""

import sys
import logging

root = logging.getLogger()
root.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


h1 = logging.StreamHandler(sys.stdout)
h1.setLevel(logging.DEBUG)
h1.setFormatter(formatter)

h2 = logging.FileHandler("8.log")
h2.setLevel(logging.DEBUG)
h2.setFormatter(formatter)

root.addHandler(h1)
root.addHandler(h2)


root.debug("go to both")
