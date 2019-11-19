#!/bin/bash

PORT=8888

while getopts p: OPT; do
    case ${OPT} in
        p) PORT=${OPTARG} ;;
    esac
done

echo "sample/python/run.sh"
shift 1;

DOCKER=/usr/local/bin/docker
${DOCKER} run --rm -v /Users/hotoku/sample/python:/root/work -p ${PORT}:${PORT} \
       hotoku/python "$@"
