#!/usr/bin/python3
''' A script that fetches alx-intranet.hbtn.io/status'''


if __name__ == '__main__':
    from urllib.request import urlopen
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as res:
        body = res.read()
    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
    print('\t- utf8 content: {}'.format(body.decode('utf-8')))
