#!/bin/bash

mkdir /hotoku
echo $(date) >> /hotoku/startup
echo $(whoami) >> /hotoku/startup
echo $(pwd) >> hotoku/startup

apt update
apt install -y python3 python3-pip emacs

## bazel
# cf: https://docs.bazel.build/versions/1.0.0/install-ubuntu.html
apt install -y pkg-config zip g++ zlib1g-dev unzip python3 openjdk-8-jdk
wget https://github.com/bazelbuild/bazel/releases/download/1.0.0/bazel-1.0.0-installer-linux-x86_64.sh
chmod u+x bazel-1.0.0-installer-linux-x86_64.sh
./bazel-1.0.0-installer-linux-x86_64.sh 2>&1 | tee /hotoku/bazel.log
