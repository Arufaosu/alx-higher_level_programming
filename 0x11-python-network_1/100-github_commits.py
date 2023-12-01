#!/usr/bin/python3
import requests
import sys

""" takes 2 arguments in order to solve this challenge """
if len(sys.argv) != 3:
    print("Usage: python script_name.py <repository_name> <owner_name>")
    sys.exit(1)

repository_name = sys.argv[1]
owner_name = sys.argv[2]

url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

response = requests.get(url)

if response.status_code == 200:
    commits = response.json()[:10]

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

else:
    print("Error:", response.status_code)
