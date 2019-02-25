#!/bin/bash
if [ -z "$1" ]; then
    echo "You must give function name as the first argument."
else
    cd ./lambda
    zip function.zip -r -j $1 --exclude *.idea*
    aws lambda update-function-code --function-name $1 --zip-file fileb://function.zip
    rm -f function.zip
    cd ../
fi