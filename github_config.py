""" If starting work on a new machine:
Create a JSON file called github_credentials.json
Give it the properties of username, github_api and personal_access_token
username: your GitHub username
github_api: the URL of GitHub's API. This shouldn't change ever but it's not impossible.
personal_access_token: obtained from https://github.com/settings/tokens
"""

import json

with open('github_credentials.json', 'r') as json_file:
    creds=json_file.read()

credentials = json.loads(creds)

USERNAME = credentials['username']
GITHUB_API = credentials['github_api']
HEADERS = 'Authorization: token {}'.format(credentials['personal_access_token'])
PARAMS = ''