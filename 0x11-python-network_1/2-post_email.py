#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

""" sends a POST request """
if len(sys.argv) != 3:
    print("Usage: python script_name.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data=data) as response:
    body = response.read().decode('utf-8')
    print("Your email is:", email)
    print(body)
