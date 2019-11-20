#/bin/bash 

DOCKER=/usr/local/bin/docker
${DOCKER} run -d --rm -e PASSWORD=hotoku -v /Users/hotoku/sample/r:/home/rstudio -p 8787:8787 hotoku/r
