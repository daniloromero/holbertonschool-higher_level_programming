#!/usr/bin/python3
"""script takes Github (username and token) uses Github API to display id"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        repo = sys.argv[1]
        owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)
    answer = r.json()
    if answer:
        for i in answer[:10]:
            sha = i.get('sha')
            commit = i.get('commit')
            if commit:
                committer = commit.get('commiter')
            print('{}: {}'.format(sha, committer.get('name')))
    else:
        print('None')
