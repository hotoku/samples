#!/bin/bash

PORT=3838
while getopts p: OPT; do
    case ${OPT} in
        p) PORT=${OPTARG} ;;
        *) exit 1 ;;
    esac
done

docker run --rm -p ${PORT}:3838 \
       -v $(pwd):/srv/shiny-server/app \
       hotoku/shiny
