#!/bin/bash
# get the status code only
if ( $# -gt 0 ) then
    curl -sL "$1"
fi
