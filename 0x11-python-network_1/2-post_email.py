#!/usr/bin/python3
"""Sending an email
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    ag_url = sys.argv[1]
    e_value = {"email": sys.argv[2]}
    en = urllib.parse.urlencode(e_value).encode("ascii")

    requ = urllib.request.Request(ag_url, en)
    with urllib.request.urlopen(requ) as resp:
        print(resp.read().decode("utf-8"))
