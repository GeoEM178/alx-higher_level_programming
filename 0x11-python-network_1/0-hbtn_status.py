#!/usr/bin/python3
"""A script to print the request data
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        title = "Body response:"
        content_type = "\t- type: {}".format(type(content))
        content = "\t- content: {}".format(content)
        decoded_con = "\t- utf8 content: {}".format(content.decode('utf-8'))
        print(title)
        print(content_type)
        print(content)
        print(decoded_con)
