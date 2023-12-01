#!/usr/bin/python3
import requests

""" sends a request to the URL """
url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

print("Body response:")
print("    - type:", type(response.text))
print("    - content:", response.text)
