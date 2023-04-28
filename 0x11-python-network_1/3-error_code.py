#!/usr/bin/python3
""" URL"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            s = response.read()
            print(s.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
