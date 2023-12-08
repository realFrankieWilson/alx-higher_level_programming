#!/usr/bin/python3
""" A script that takes in a URL, sends a POST request to te URL and displays
    to the  found in the header of the
    response
"""


if __name__ == "__main__":
    # Import the necessary libraries.
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    # Email is parsed from command line
    email = argv[2]
    # Email is mapped to a dictionary
    my_dict = {'email': email}
    # Turn data to bytes
    data = urlencode(my_dict).encode('utf-8')
    url = Request(argv[1], data)
    with urlopen(url) as r:
        print(r.read().decode('utf-8'))
