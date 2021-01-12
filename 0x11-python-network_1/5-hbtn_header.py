#!/usr/bin/python3
"""script takes in URL, sends request to URL, displays value of X-Request-Id"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    answer = r.headers.get('X-Request-Id')
    print(answer)
