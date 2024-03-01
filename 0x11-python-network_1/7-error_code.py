#!/usr/bin/python3
"""A script that send req and display body
"""
import sys
import requests


if __name__ == "__main__":
    arg_url = sys.argv[1]

    requ = requests.get(arg_url)
    fixed_num = 400
    if requ.status_code >= fixed_num:
        print(f"Error code: {requ.status_code}")
    else:
        print(requ.text)
