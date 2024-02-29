#!/bin/bash
# Send post request with values
if ( $# -gt 0 ) then
    curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
fi

