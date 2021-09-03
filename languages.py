#############################################################################
# Use the list below to determine which languages you will be working with, #
# then run this file to grab the language extensions and put them into      #
# languages.json for the rest of this program to use.                       #
#############################################################################
languages = [
    'C','C++','C#','Go','Java','JavaScript','PHP','Python','Rust','TypeScript'
]

import requests
import json

# Make sure you get the raw URLs, not the URLs of the pages Git shows you!

language_gist_url = "https://gist.githubusercontent.com/ppisarczyk/43962d06686722d26d176fad46879d41/raw/211547723b4621a622fc56978d74aa416cbd1729/Programming_Languages_Extensions.json"
backup_language_gist_url = "https://gist.githubusercontent.com/aymen-mouelhi/82c93fbcd25f091f2c13faa5e0d61760/raw/465a579aec8d3c04a8d201f9364b1feafd509d31/languages.json"

def main():
    try:
        r = requests.get(language_gist_url).json()
    except:
        r = requests.get(backup_language_gist_url).json()

    extensions = [l for l in r if l['name'] in languages]

    f = open('languages.json','w')
    if f.mode == 'w':
        f.write(json.dumps(extensions))
        f.close()

if __name__ == '__main__':
    main()