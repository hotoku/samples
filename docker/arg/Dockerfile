FROM ubuntu:latest
# FROM python:3.8.3-buster

WORKDIR /work
COPY run.sh /work
ENTRYPOINT ["/work/run.sh"]

# NOT: If ENTRYPOINT is /work/run.sh (not enclosed with bracket,
# we can not pass arguments from docker run command.
