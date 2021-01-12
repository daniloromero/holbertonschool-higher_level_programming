#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""


if __name__ == '__main__':
    import urllib.request
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        answer = response.info().get('X-request-Id')
        print(answer)
