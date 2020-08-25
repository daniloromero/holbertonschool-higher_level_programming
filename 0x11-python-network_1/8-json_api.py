#!/usr/bin/python3
"""sends a POST request with the email as a parameter"""
import requests
import sys


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        data = { 'q': sys.argv[1]}
    else:
        data = {'q': ""}
    try:
        r = requests.post(url, data)
        body =r.json()
        if body:
            print(' {{} {}'.format(js.body.get('id'), body.get('name')))
        else:
            print("No result")
    except ValueError:
        print('Not a valid JSON')
