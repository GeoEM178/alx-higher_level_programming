#!/bin/bash
# send with delete reqdisable prog
if ( $# -lt 1 ) then
    echo "No arguments supplied"
    exit 1
fi
curl -sX DELETE "$1"
