#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    from sys import argv
    import requests
    user = argv[1]
    pssword = argv[2]
    url = "https://api.github.com/user"

    req = requests.get(url, auth=(user, pssword))
    req_json_rep = req.json()

    print(req_json_rep.get("id", "None"))
