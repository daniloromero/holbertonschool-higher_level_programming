#!/usr/bin/python3
"""sends a URL  request and displays the body of response"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    answer = r.status_code
    if answer >= 400:
        print('Error code: {}'.format(answer))
    else:
        print(r.text)
