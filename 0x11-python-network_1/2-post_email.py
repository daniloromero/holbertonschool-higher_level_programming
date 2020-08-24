#!/usr/bin/python3
"""sends a POST request with the email as a parameter"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    data = urllib.parse.urlencode({'email': sys.argv[1]})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        answer = response.read().decode('utf-8')
        print(answer)
