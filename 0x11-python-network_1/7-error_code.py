#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL and displays the body of the response."""

if __name__ == "__main__":
    from sys import argv
    import requests

    igede = requests.get(argv[1])

    if igede.status_code >= 400:
        print(igede.text)
    else:
        print("Error code", igede.status_code)
