#!/usr/bin/python3
'''
   A script that takes 2 arguments in order to solve a challenge.
   and uses the github api to dispaly the commits.
'''

if __name__ == '__main__':
    import requests
    from sys import argv

    # Github API
    api = 'https://api.github.com/repos/{}/commits/{}'.format(
            argv[1], argv[2])

    resp = requests.get(api)
    # Extract the commits from the response.
    commits = resp.json()
    try:
        # Loop through the commits
        for i in range(10):
            print(
                    "{}: {}".format(
                        commits[i].get("sha"),
                        commits[i].get("commit").get("author").get("name")
                        )
                    )
    except IndexError:
        pass
