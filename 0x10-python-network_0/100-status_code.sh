#!/bin/bash
# Output or prrint the status code
curl -s -w "%{http_code}" -o /dev/null "$1"
