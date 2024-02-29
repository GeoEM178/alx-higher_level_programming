#!/bin/bash
# Output or prrint the status code
if ( $# -lt 1 ) then
    echo "No arguments supplied"
    exit 1
fi
curl -s -w "%{http_code}" -o /dev/null "$1"
