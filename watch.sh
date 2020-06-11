#!/bin/bash

fileToRun=$1

echo $fileToRun
if [ -z $fileToRun ]; then 
    echo "Usage: ./watch.sh <name_of_file>"; 
else
     ls | entr -c python3 ./692-top-k-frequent-words.py;
fi

