#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == '__main__':
        url = 'https://intranet.hbtn.io/status'
        r = requests.get(url)
        answer = r.text
        print('Body response:')
        print('\t- type: {}'.format(type(answer)))
        print('\t- content: {}'.format(answer))
