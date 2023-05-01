#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request to 
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    if len(.argv) > 0:
        q = argv[1]
    else:
        q = ""

    try:
        url = "http://0.0.0.0:5000/search_user"
        payload = {"q": q}
        req = requests.post(url, payload).json()

        if len(req) > 0:
            print("{[]} {}".format(req.get("id"), req.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
