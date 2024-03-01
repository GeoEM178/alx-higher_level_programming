#!/usr/bin/python3
"""Printinf data
"""
import sys
import urllib.request

if __name__ == "__main__":
    arg_url = sys.argv[1]

    requ = urllib.request.Request(arg_url)
    with urllib.request.urlopen(requ) as resp:
        res = dict(resp.headers).get("X-Request-Id")
        print(res)
