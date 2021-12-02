#!/bin/bash


cat <<EOF | xargs -I@ -n1 echo @
a
b
c
d
EOF
