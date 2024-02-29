#!/bin/bash
# show what are allowed
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
