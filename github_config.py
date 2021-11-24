""" If starting work on a new machine:
Create a JSON file called github_credentials.json
Give it the properties of username, github_api and personal_access_token
username: your GitHub username
github_api: the URL of GitHub's API. This shouldn't change ever but it's not impossible I suppose.
personal_access_token: obtained from https://github.com/settings/tokens
"""

import json

def get_credentials():
    with open('github_credentials.json', 'r') as json_file:
        creds=json_file.read()

    credentials = json.loads(creds)
    json_file.close()
    return credentials

credentials = get_credentials()

USERNAME = credentials['username']
GITHUB_API = credentials['github_api']
HEADERS = 'Authorization: token {}'.format(credentials['personal_access_token'])
PARAMS = ''

if __name__ == '__main__':
    print("This script is not to be run standalone.")