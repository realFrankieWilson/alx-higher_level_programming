#!/usr/bin/python3
'''
   A script that takes in a URL, Sends a request to the url and displays the
   body of the response.
'''

if __name__ == '__main__':
    # Import the necessary packages/modules
    from sys import argv
    import requests

    # Get the url
    url = requests.get(argv[1])
    if (int(url.status_code) >= 400):
        print("Error code: {}".format(url.status_code))
    else:
        print(url.text)
