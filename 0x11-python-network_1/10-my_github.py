#!/usr/bin/python3
"""script takes Github (username and token) uses Github API to display id"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == '__main__':
    url = ' https://api.github.com' 
    if len(sys.argv) > 1:
        username = sys.argv[1]
        password = sys.argv[2]
    else:
        data = {'q': ""}
    r = requests.post(url, auth=HTTPBasicAuth(username, password)
    answer = r.json()
    if answer:
        print('{}'.format(answer.get('user')))
    else:
        print('None')
