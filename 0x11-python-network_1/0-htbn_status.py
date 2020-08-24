#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""


if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        answer = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(answer)))
        print('\t- content: {}'.format(answer))
        print('\t- utf8 content: {}'.format(answer.decode()))