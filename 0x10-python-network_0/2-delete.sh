#!/bin/bash
# send with delete reqdisable prog
if ( $# -gt 0 ) then
    curl -sX DELETE "$1"
fi

