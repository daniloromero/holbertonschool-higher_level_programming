#!/usr/bin/python3
"""script takes Github (username and token) uses Github API to display id"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    if len(sys.argv) > 1:
        username = sys.argv[1]
        password = sys.argv[2]
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    answer = r.json()
    if answer:
        print('{}'.format(answer.get('id')))
    else:
        print('None')
