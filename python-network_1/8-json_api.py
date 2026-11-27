#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        r = requests.post(url, data=payload)
        json_obj = r.json()
        if json_obj:
            print("[{}] {}".format(json_obj.get('id'), json_obj.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
