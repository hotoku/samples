#!/bin/bash

mkdir /hotoku
echo $(date) >> /hotoku/startup
echo $(whoami) >> /hotoku/startup

apt update
apt install -y python3 python3-pip emacs
