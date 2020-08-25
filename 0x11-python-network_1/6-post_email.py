#!/usr/bin/python3
"""sends a POST request with the email as a parameter"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.post(url, data={'email': sys.argv[2]})
    body = r.text
    print(body)
