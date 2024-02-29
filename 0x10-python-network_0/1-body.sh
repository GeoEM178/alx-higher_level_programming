#!/bin/bash
# get the status code only
if ( $1 ) then
    curl -sL "$1"
fi

