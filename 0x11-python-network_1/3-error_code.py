#!/usr/bin/python3
""" A script that takes in a URL, sends a request to te URL and displays
    the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    # Import the necessary libraries.
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    # Url parsed from command line
    url = argv[1]
    with urlopen(url) as r:
        resp = r.read().decode('utf-8')
    print(resp)