#!/bin/bash
# get data by bytes only
curl -s "$1" | wc -c
