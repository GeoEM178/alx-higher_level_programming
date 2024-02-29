#!/bin/bash
# Make a post req with type json
if ( $# -lt 2 ) then
    echo "No arguments supplied"
    exit 1
fi
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
