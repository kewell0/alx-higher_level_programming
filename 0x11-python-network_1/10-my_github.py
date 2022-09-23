#!/usr/bin/python3
"""
 Takes your GitHub credentials (username and password) and
 uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    resp = requests.get(url, auth=(argv[1], argv[2]))
    json = resp.json()
    if json == {}:
        print("None")
    else:
        print("{}".format(json.get('id')))
