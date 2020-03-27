import json

import json
from io import StringIO

sio = StringIO()
json.dump(set([1, 2, 3]), sio)  # setはjsonにできない

print(sio.value)
