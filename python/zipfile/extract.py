#!/usr/bin/env python3


import zipfile
with zipfile.ZipFile("1.zip", 'r') as zip_ref:
    zip_ref.extractall(".")
