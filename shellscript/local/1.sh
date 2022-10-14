#!/bin/bash


f(){
    p=$1 # localを付けないと、外の変数にも影響を及ぼす
}


g(){
    local p=$1
}


h(){
    local p=ho
    p=${p}ge # 最初にlocalで宣言されていれば、あとで代入してもlocalのまま
}


p=10
echo $p
f 1
echo $p
g 10
echo $p


h
echo $p
