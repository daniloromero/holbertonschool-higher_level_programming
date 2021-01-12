#!/usr/bin/python3
"""script takes in URL, sends request to URL, displays value of X-Request-Id"""
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    try:
        r = requests.post(url, data)
        answer = r.json()
        if answer:
            print('[{}] {}'.format(answer.get('id'), answer.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
