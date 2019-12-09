#!/bin/bash

PORT=3838
while getopts p: OPT; do
    case ${OPT} in
        p) PORT=${OPTARG} ;;
        *) exit 1         ;;
    esac
done


DOCKER=/usr/local/bin/docker
${DOCKER} run --rm -p ${PORT}:3838 \
       hotoku/shiny_sample
