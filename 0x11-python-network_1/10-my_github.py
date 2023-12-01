#!/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth
import sys

""" uses the GitHub API to display your id """
if len(sys.argv) != 3:
    print("Usage: python script_name.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

url = "https://api.github.com/user"

response = requests.get(url, auth=HTTPBasicAuth(username, token))

if response.status_code == 200:
    try:
        data = response.json()
        print(data.get('id'))
    except ValueError:
        print("Not a valid JSON")
else:
    print("Error code:", response.status_code)
