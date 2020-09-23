#!/bin/bash

cat 1.json | jq '.[] | select(.id|test("a."))'
