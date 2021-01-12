#!/usr/bin/python3
"""script a POST request with the email as a parameter"""
from urllib.request import urlopen
from urllib.error import HTTPError
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            answer = response.read().decode('utf-8')
            print(answer)
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
