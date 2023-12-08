#!/usr/bin/python3
'''
   A script that takes in a letter and sends a POST request to a url
   with the letter as a parameter.
'''

if __name__ == '__main__':
    import requests
    from sys import argv

    # A string string
    q = ""

    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    my_dict = {'q': q}
    url = requests.post('http://0.0.0.0:5000/search_user', my_dict)

    try:
        resp = url.json()
        if len(resp) == 2:
            print("[{}] {}".format(resp['id'], resp['name']))
        else:
            print('No result')
    except ValueError:
        print("Not a valid JSON")
