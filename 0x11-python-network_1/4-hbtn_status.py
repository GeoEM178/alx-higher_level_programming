#!/usr/bin/python3
"""interanet link"""
import requests


if __name__ == "__main__":
    arg_url = "https://intranet.hbtn.io/status"
    requ = requests.get(arg_url)
    print("Body response:")
    print(f"\t- type: {type(requ.text)}")
    print(f"\t- content: {requ.text}")
