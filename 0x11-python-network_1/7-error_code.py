#!/usr/bin/python3
"""will send request to a link and display the response.
Usage: ./7-error_code.py <URL>
  - handels HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
