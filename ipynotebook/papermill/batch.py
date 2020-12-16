#!/usr/bin/env python


import papermill as pm

pm.execute_notebook(
    "./sample.ipynb",
    "./output.ipynb",
    parameters={"X": 1000, "S": "xyz"}
)
