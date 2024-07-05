#!/usr/bin/python3
"""Uses github to display GitHub ID based on given creds.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - uses auth to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
