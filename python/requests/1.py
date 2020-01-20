#!/usr/bin/env python


import requests
import json
import sys


url = "https://reqres.in/api/users"
ret = requests.get(url)
print(json.dump(ret.json(), sys.stdout))
