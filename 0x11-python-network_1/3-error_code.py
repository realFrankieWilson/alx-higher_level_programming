#!/usr/bin/python3
""" A script that takes in a URL, sends a request to te URL and displays
    the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    # Import the necessary libraries.
    from urllib.error import HTTPError
    from urllib.request import urlopen
    from sys import argv

    # Url parsed from command line
    url = argv[1]

    try:
        # Send a Get request
        with urlopen(url) as r:
            resp = r.read().decode('utf-8')

        # Display contents
        print(resp)

        # Handles HTTP error
    except HTTPError as e:
        print("Error code: {}".format(e.code))
