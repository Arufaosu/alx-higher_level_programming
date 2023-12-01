#!/usr/bin/python3
import requests
import sys

"""  sends a POST request """
if len(sys.argv) != 3:
    print("Usage: python script_name.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

response = requests.post(url, data={'email': email})

print("Your email is:", email)
print(response.text)
