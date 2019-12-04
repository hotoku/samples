#/bin/bash 


PORT=8787
while getopts p: OPT; do
    case ${OPT} in
        p) PORT=${OPTARG} ;;
        *) exit 1         ;;
    esac
done

DOCKER=/usr/local/bin/docker
${DOCKER} run -d --rm -e PASSWORD=hotoku -v /Users/hotoku/sample/r:/home/rstudio -p ${PORT}:8787 hotoku/r
