#!/usr/bin/python3
"""script takes a URL, sends request to URL, displays value of X-Request-Id""" 
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        answer = response.info().get('X-request-Id')
        print(answer)
