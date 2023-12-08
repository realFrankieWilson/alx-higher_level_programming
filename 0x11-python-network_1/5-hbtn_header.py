#!/usr/bin/python3
'''
    A script that takes in a URL, sends a request to the url and displays
    the value of the variable X-Request-Id in the response header.
    Using the requests package.
'''


if __name__ == '__main__':
    # Import the necessary packages.
    import requests
    from sys import argv

    # Get the url from command prompt
    url = requests.get(argv[1])

    # Display content
    print(url.headers.get('X-Request-Id'))
