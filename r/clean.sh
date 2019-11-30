#!/bin/bash

cat <<EOF | xargs rm -rf
.Rhistory
.bash
.config
.rstudio
kitematic
EOF
