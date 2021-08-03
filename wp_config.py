""" If starting work on a new machine:
Create a JSON file called wp_credentials.json
Give it the properties of password, user and wp_api
password: obtain an application password from your Wordpress interface
user: Your username when logging into WordPress
wp_api: The URL of your WordPress instance's API
"""

import base64
import json

with open('wp_credentials.json', 'r') as json_file:
    creds=json_file.read()

credentials = json.loads(creds)

URL = credentials['wp-api']

user = credentials['user']
password = credentials['password']
auth_string = user + ':' + password
token = base64.b64encode(auth_string.encode())
HEADERS = {'Authorization': 'Basic ' + token.decode('utf-8')}