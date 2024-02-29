#!/bin/bash
# get the status code only
if ( $# -lt 1 ) then
    echo "No arguments supplied"
    exit 1
fi
curl -sL "$1"
