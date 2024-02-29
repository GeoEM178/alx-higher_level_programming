#!/bin/bash
# Make a post req with type json
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
