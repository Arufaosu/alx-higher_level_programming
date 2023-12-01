#!/usr/bin/python3
import urllib.request
import sys

""" takes in a URL, sends a request """
if len(sys.argv) != 2:
    print("Usage: python script_name.py <URL>")
    sys.exit(1)

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.getheader('X-Request-Id')
    print(x_request_id)
