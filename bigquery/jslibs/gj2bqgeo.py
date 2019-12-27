#!/usr/bin/env python


import json
from io import StringIO
import sys
import argparse


def swap(pair):
    return pair[1], pair[0]


class Polygon:
    def __init__(self, obj):
        self.coordinates = obj["coordinates"]

    def __str__(self):
        if len(self.coordinates) > 1:
            raise Exception(
                "Polygon with more than 1 coordinates can not be handled")
        points = self.coordinates[0]
        return "POLYGON((" + ", ".join(["{} {}".format(p[0], p[1]) for p in points]) + "))"


class App:
    types = dict(
        Polygon=Polygon
    )

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("file")

    def run(self):
        args = self.parser.parse_args()
        return self.transform(open(args.file))

    def transform(self, io):
        featuers = json.load(io)["features"]
        ret = []
        for f in featuers:
            geometry = f["geometry"]
            type_ = geometry["type"]
            ret.append(str(self.types[type_](f["geometry"])))
        return ret


if __name__ == "__main__":
    ls = App().run()
    for s in ls:
        print(s)
