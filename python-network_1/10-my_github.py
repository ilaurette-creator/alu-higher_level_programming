#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and password/PAT)
and uses the GitHub API to display your id.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(username, password))
    try:
        print(r.json().get("id"))
    except ValueError:
        print("None")
