#!/usr/bin/python3
"""Send an email
"""
import sys
import requests

if __name__ == "__main__":
    person_to_send = {'email': sys.argv[2]}
    try:
        arg_url = sys.argv[1]
        response = requests.post(arg_url, data=person_to_send)
        print(f"Your email is: {person_to_send}")
    except requests.exceptions.RequestException as eror:
        print(f"Error: {eror}")
