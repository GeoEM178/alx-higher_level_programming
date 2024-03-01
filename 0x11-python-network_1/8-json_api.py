#!/usr/bin/python3
"""Using JSON API
"""
import sys
import requests


if __name__ == "__main__":
    sing_l = "" if len(sys.argv) == 1 else sys.argv[1]
    one_l = {"q": sing_l}
    fixed_url = "http://0.0.0.0:5000/search_user"

    req = requests.post(fixed_url, data=one_l)
    try:
        rersp = req.json()
        if rersp == {}:
            print("No result")
        else:
            print(f"[{rersp.get("id")}] {rersp.get("name")}")
    except ValueError:
        print("Not a valid JSON")
