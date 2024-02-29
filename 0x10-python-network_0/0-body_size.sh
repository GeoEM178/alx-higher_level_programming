#!/bin/bash
# get data by bytes only
if ( $# -lt 1 ) then
    echo "No arguments supplied"
    exit 1
fi
curl -s "$1" | wc -c
