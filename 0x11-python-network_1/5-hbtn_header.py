#/!usr/bin/python3
"""script takes in URL, sends request to URL, displays value of X-Request-Id"""
import request
import sys


if __name ==' __main__':
    url = sys.argv[1]
    r = request.get(url)
    answer = r.request.get('X-Request-Id')
    print(answer)
