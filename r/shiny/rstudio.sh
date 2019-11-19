#!/bin/bash

PORT=8787
while getopts p: OPT; do
    case ${OPT} in
        p) PORT=${OPTARG} ;;
        *) exit 1 ;;
    esac
done

docker run -it \
       --rm \
       -e PASSWORD=hotoku \
       -v $(pwd):/home/rstudio \
       -p ${PORT}:8787 hotoku/r
