#!/usr/bin/python3
'''
   A script that takes a github credentials(username and password)
   and uses the github api to dispaly the id.
'''

if __name__ == '__main__':
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    # Github API
    api = 'https://api.github.com/user'
    # Authenticate the values passed
    auth = HTTPBasicAuth(argv[1], argv[2])

    resp = requests.get(api, auth=auth)
    # Extract the id from the response.
    my_id = resp.json().get('id')
    # Display the id
    print(my_id)
