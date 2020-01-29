#!/bin/bash

f(){
    p=$1 # localを付けないと、外の変数にも影響を及ぼす
}

g(){
    local p=$1
}


p=10
echo $p
f 1
echo $p
g 10
echo $p
