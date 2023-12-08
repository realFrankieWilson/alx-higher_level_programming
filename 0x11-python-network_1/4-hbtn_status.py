#!/usr/bin/python3
'''
    A script that fetches https://alx-intranet.hbtn.io/status
    using the requests package.
'''


if __name__ == '__main__':
    # Import the necessary packages.
    import requests

    # Making request and saving the obj in res
    url = requests.get('https://alx-intranet.hbtn.io/status')
    # Displaying the response.
    print("Body response:")
    print("\t- type: {}".format(type(url.text)))
    print("\t- content: {}".format(url.text))
