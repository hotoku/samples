#!/bin/bash

while getopts abc: OPT; do
    case ${OPT} in
        a) A=1 ;;
        b) B=1 ;;
        c) C=${OPTARG} ;;
        ?) print_usage; exit ;;
    esac
done

echo A=${A} B=${B} C=${C}
