#!/usr/bin/python3
""" A script that takes in a URL, sends a request to te URL and displays
    the value of te X-Request-Id variables found in the header of the response
"""


if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv
    url = argv[1]
    with urlopen(url) as resp:
        body = resp.headers
    print("{}".format(body.get("X-Request-Id")))
