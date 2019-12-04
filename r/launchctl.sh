#!/bin/bash -l


while ! docker ps; do
    echo $(date) "waiting for docker to launch ..."
    sleep 1
done

/Users/hotoku/samples/r/run.sh -p 9002
