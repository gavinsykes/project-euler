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

  for e in extensions:
    if len(e['extensions']) == 1:
      print('\x1b[1;32;40m' + f"Only one extension found for {e['name']}: \"{e['extensions'][0]}\", setting it as the main one." + '\x1b[0m')
      e['main'] = e['extensions'][0]
      continue
    inp = input(f"The listed extensions for {e['name']} are {e['extensions']}, which one is the main one?\n")
    while not inp in e['extensions']:
      print('\x1b[1;31;40m' + f"Sorry, it seems \"{inp}\" isn't one of the listed extensions for {e['name']}." + '\x1b[0m')
      print(f"The extensions are {e['extensions']} for {e['name']}.")
      inp = input("Which one do you want to use?\n")
    e['main'] = inp

  with open('languages.json','w') as language_json:
    language_json.write(json.dumps(extensions))

if __name__ == '__main__':
  main()