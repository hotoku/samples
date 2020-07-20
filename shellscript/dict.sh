#!/usr/local/bin/bash

declare -A exam
exam["a"]=1
exam["b"]=2


a=a
b=b
echo ${exam[$a]} ${exam[$b]}
