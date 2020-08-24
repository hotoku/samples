#!/bin/bash

list_options(){
    echo a b c
    echo d e f
}

list_options | parallel --colsep " " echo {3} {2} {1}

