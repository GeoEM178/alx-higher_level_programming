#!/usr/bin/python3
"""A script that uses gitHub api
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]
    auth_data = HTTPBasicAuth(usr, passwd)
    req = requests.get("https://api.github.com/user", auth=auth_data)
    print(req.json().get("id"))
