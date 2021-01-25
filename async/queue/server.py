#!/usr/bin/env python3


import bottle
from bottle import route, request, HTTPResponse
import json
import time


port = 9100
host = "localhost"


@route("/")
def root():
    prm = request.query.prm
    if not prm:
        k, v = "0", "0"
    else:
        k, v = prm.split("-")
    key = int(k)
    if key >= 5:
        ret = {
            "done": True,
            "v": v
        }
    else:
        ret = {
            "key": key + 1,
            "v": [v + "_" + str(i) for i in range(3)]
        }
    header = {
        "Content-Type": "application/json"
    }
    body = json.dumps(ret)
    time.sleep(0.5)
    return HTTPResponse(status=200, body=body, headers=header)


bottle.run(host=host, port=port, reloader=True, server="paste")
