#!/bin/bash
# Send with hedear
if ( $# -lt 1 ) then
    echo "No arguments supplied"
    exit 1
fi
curl -sH "X-School-User-Id: 98" "${1}"
