#!/bin/bash
# show what are allowed
if ( $# -lt 1 ) then
    echo "No arguments supplied"
    exit 1
fi
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
