#!/bin/bash
# get data by bytes only
if ( $# -gt 0) then
    curl -s "$1" | wc -c
fi
