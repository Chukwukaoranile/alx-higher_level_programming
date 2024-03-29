#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as fet:
        html = fet.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
