#!/usr/bin/python3
'''
    A script that takes in a URL and an email address, sends a POST request to
    the passed URL with the email as a parameter, and displays the body of
    the response.
'''


if __name__ == '__main__':
    import requests
    from sys import argv

    email = {'email': argv[2]}
    resp = requests.post(argv[1], email)
    # print contents
    print(resp.text)
