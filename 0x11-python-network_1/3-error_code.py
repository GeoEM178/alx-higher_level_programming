#!/usr/bin/python3
"""Sending errror status code
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        arg_url = sys.argv[1]
        with request.urlopen(arg_url) as boddy:
            print(boddy.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
