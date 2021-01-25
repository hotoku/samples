#!/usr/bin/env python3


import requests


def get(url):
    resp = requests.get(url)
    ret = resp.json()
    if "done" in ret:
        print(ret["v"])
        return
    else:
        key = ret["key"]
        v = ret["v"]
        for v_ in v:
            get(f"http://localhost:9100?prm={key}-{v_}")


url = "http://localhost:9100"
get(url)
