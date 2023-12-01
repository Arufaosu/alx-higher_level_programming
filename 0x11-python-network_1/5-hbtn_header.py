#!/usr/bin/python3
import requests
import sys

""" displays the value of the variable X-Request-Id """
if len(sys.argv) != 2:
    print("Usage: python script_name.py <URL>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)

x_request_id = response.headers.get('X-Request-Id', None)

if x_request_id:
    print(x_request_id)
