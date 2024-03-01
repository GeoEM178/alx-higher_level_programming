#!/usr/bin/python3
"""list commits
"""
import sys
import requests


if __name__ == "__main__":
    ar1 = sys.argv[1]
    ar2 = sys.argv[2]
    gh_url = f"https://api.github.com/repos/{ar2}/{ar1}/commits"
    requ = requests.get(gh_url)
    gh = requ.json()
    try:
        for i in range(10):
            gh_c = gh[i].get("sha")
            gh_A = gh[i].get("commit").get("author").get("name")
            print(f"{gh_c}: {gh_A}")
    except Exception:
        pass
