#!/usr/bin/python3
"""script takes Github (username and token) uses Github API to display id"""
import requests
import sys


if __name__ == '__main__':
    url = ' https://api.github.com' 
    if len(sys.argv) > 1:
        data = {'username': sys.argv[1],
                'password': sys.argv{2}}
    else:
        data = {'q': ""}
    try:
        r = requests.post(url, data)
        answer = r.json()
        if answer:
            print('{}'.format(answer.get('user')))
        else:
            print('None')
    except ValueError:
        print('Not a valid JSON')
