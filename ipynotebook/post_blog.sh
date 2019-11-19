#!/bin/bash



print_usage(){
    echo "./post_blog.sh <ipynby file path> <title>"
}


file=$1
title=$2

if [ -z "${file}" ] || [ -z "${title}" ]; then
    print_usage
    exit 1
fi
 
source activate jupy2wp
python -m jupy2wp.jupy2wp --xmlrpc-url https://www.hotoku.info/xmlrpc.php --user user --password jRqLp81PIf9z --nb ${file} --title ${title} --categories python --template basicx
conda deactivate
