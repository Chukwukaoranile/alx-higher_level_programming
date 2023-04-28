#!/usr/bin/python3
"""
A Python script that takes 2 arguments in order to solve this challenge.

- The first argument will be the repository name
- The second argument will be the owner name
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to check arguments passed to the script (number or type)
"""
if __name__ == "__main__":
    from sys import argv
    import requests
    url = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    r = requests.get(url)
    git_commits = r.json()
    try:
        for count in range(10):
            print("{}: {}".format(
                git_commits[count].get("sha"),
                git_commits[count].get("commit").get("author").get("name")))
    except IndexError:
        pass
