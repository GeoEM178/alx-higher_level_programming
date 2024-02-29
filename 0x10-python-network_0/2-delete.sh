#!/bin/bash
# send with delete reqdisable prog
if ( $1 ) then
    curl -sX DELETE "$1"
fi

