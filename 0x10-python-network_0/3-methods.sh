#!/bin/bash
# show what are allowed
if ( $1 ) then
    curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
fi
