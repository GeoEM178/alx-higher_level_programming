#!/usr/bin/python3
"""Print header Data
"""
import sys
import requests


if __name__ == "__main__":
    arg_url = sys.argv[1]

    req = requests.get(arg_url)
    h_data = req.headers.get("X-Request-Id")
    print(h_data)
