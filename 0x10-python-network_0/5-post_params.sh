#!/bin/bash
# Send post request with values
if ( $# -lt 1 ) then
    echo "No arguments supplied"
    exit 1
fi
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
