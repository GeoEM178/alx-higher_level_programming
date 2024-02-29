#!/bin/bash
# get data by bytes only
if ( $1 ) then
    curl -s "$1" | wc -c
fi

