#!/usr/bin/env python

from glob import glob
import json
import requests
import pandas as pd
from tqdm import tqdm


def _key():
    return open("key.txt").readline().strip()


KEY = _key()
URL = "https://maps.googleapis.com/maps/api/geocode/json"
DIR = "jalan/data"


def get(f):
    with open(f) as f2:
        obj = json.load(f2)
    a1 = obj["address"]
    a2 = " ".join(a1.split(" ")[1:])
    resp = requests.get(URL, params=dict(
        key=KEY,
        address=a2))
    ret = resp.json()
    try:
        ret2 = ret["results"][0]["geometry"]["location"]
        obj = dict(obj, **ret2)
    except IndexError:
        obj["lat"] = None
        obj["lng"] = None
    obj["geocoding"] = ret
    return obj


def main():
    key = _key()
    ret = [
        get(f)
        for f in tqdm(glob(f"./{DIR}/spt_*"))
    ]
    keys = ret[0].keys()
    pd.DataFrame({
        k: [ret[i][k] for i in range(len(ret))]
        for k in keys
    }).to_csv("list.csv")


if __name__ == "__main__":
    main()
