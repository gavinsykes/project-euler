import github_config as config

import copy
import os
import re
import requests
import json

# First of all, what languages will I be working in?
languages = {
  '.c':'C',
  '.cpp':'C++',
  '.java':'Java',
  '.js':'JavaScript',
  '.php':'PHP',
  '.py':'Python',
  '.rs':'Rust',
  '.ts':'TypeScript'
}

# Better download all the gists currently on my account
def get_all_gists_for_user(user):
  return requests.get(
    config.GITHUB_API + 'users/%s/gists'%user
  ).json()

# And we need to know what directory we're currently working in
workingdirectory = os.getcwd()

# Now to allow me to pick what I want to do when I run this script.
def pick_action(actions):
  print('Hi Gavin, what would you like to do with your Project Euler gists this evening?')
  for i, el in enumerate(actions):
    print('{}) {}'.format(i+1,el))
  inp = input('Make your choice: ')
  try:
    if 0 < int(inp) <= len(actions):
      return int(inp)
  except:
    pass
  return None

# possible_actions = ['Update gists','Check gists','Post new gists']

# chosen_action = pick_action(possible_actions)
# print(chosen_action)

# Pull current gists
def get_gists():
  gists = get_all_gists_for_user(config.USERNAME)
  defaultdict = {'C':'No','C++':'No','Java':'No','JavaScript':'No','PHP':'No','Python':'No','Rust':'No'}
  problems = {'1':copy.copy(defaultdict)}
  for gist in gists:
    snippets = gist['files']
    for f, d in snippets.items():
      if (re.findall('euler_problem_',d['filename'])):
        if (re.findall(r'\d+',d['filename'])):
          prob_num = re.findall(r'\d+',d['filename'])[0]
        else:
          prob_num = 0
        language = d['language']
        if prob_num not in problems.keys():
          problems[str(prob_num)] = copy.copy(defaultdict)
        problems[str(prob_num)][language] = 'Yes'
  return problems

# Given a problem, determine whether any Gists exist
def gists_exist_for_problem(problem_number):
  for gist in gists:
    files = gist['files']
    for f, d in files.items():
      if (re.findall(r'\d+',d['filename'])):
        if (re.findall(r'\d+',d['filename'])[0] == str(problem_number)):
          return True
  return False

# Given a problem and language, determine whether the gist exists
def gistexists(problem,language):
  for gist in gists:
    files = gist['files']
    for f, d in files.items():
      if (re.findall(r'\d+',d['filename'])):
        if (re.findall(r'\d+',d['filename'])[0] == str(problem)):
          if (d['language'] == language):
            return True
  return False

# Get files in repository
def fileexists(problem,language):
  try:
    os.chdir(workingdirectory + '/problem_' + str(problem))
    ext = list(languages.keys())[list(languages.values()).index(language)]
    fi = open('problem_'+str(problem)+ext,'r')
    if fi.mode == 'r':
      fi.close()
      return True
    else:
      fi.close()
      return False
  except:
    return False

# Get contents of file for given problem and language
def getfilecontents(problem,language):
  os.chdir(workingdirectory + '/problem_' + str(problem))
  ext = list(languages.keys())[list(languages.values()).index(language)]
  fi = open('problem_'+str(problem)+ext,'r')
  if fi.mode == 'r':
    contents = fi.read()
    fi.close()
    return contents
  return None

def getfiles():
  directorylist = list(filter(lambda dir: re.match(r'problem_',dir),os.listdir()))
  for directory in directorylist:
    os.chdir(workingdirectory + '/' + directory)
    for f in os.listdir():
      parts = os.path.splitext(f)
      if parts[1] in languages.keys():
        fi = open(f,'r')
        if fi.mode == 'r':
          contents = fi.read()
          fi.close()
          print(contents)

# Post a gist
def postgist(url,headers,params,data):
  requests.post(url,headers=headers,params=params,data=data)

# Create a new gist
def creategist(problem,language):
  url = config.GITHUB_API + 'gists'
  headers = config.HEADERS
  params = config.PARAMS
  filename = 'euler_problem_' + str(problem) + list(languages.keys())[list(languages.values()).index(language)]
  body = {'files':{filename:{'content':getfilecontents(problem,language)}},'public':True}
  if (not(gistexists(problem,language))):
    postgist(url,headers,params,json.dumps(body))

# Post up all the gists in all language available in the repo, given a range of problems
def postallgists():
  print('What range of gists do you want to post?')
  start = input('Enter the starting number: ')
  end = input('Enter the ending number: ')
  for i in range(int(start),int(end) + 1):
    for l, n in languages.items():
      print('Problem ' + str(i) + ' in ' + n)
      if fileexists(i,n):
        print('\x1b[2;32;40mFile exists\x1b[0m')
        if gistexists(i,n):
          print('\x1b[2;32;40mGist also exists\x1b[0m')
        else:
          print('\x1b[1;31;40mGist doesn\'t exist\x1b[0m')
          print('\x1b[2;32;40mCreating gist now...\x1b[0m')
          creategist(i,n)
      else:
        print('\x1b[1;31;40mFile doesn\'t exist\x1b[0m')
        if gistexists(i,n):
          print('\x1b[2;32;40mBut the gist does, apparently.\x1b[0m')

# Update existing gists

# Get the ID of a gist given the problem and the language
def gist_id(problem,language):
  for gist in gists:
    files = gist['files']
    for f, d in files.items():
      if (re.findall(r'\d+',d['filename'])):
        if (re.findall(r'\d+',d['filename'])[0] == str(problem)):
          if (d['language'] == language):
            return gist['id']

# Get the content of a gist given the gist's ID
def gist_contents(gist_id):
  url = config.GITHUB_API + 'gists/' + str(gist_id)
  gist = requests.get(url,headers=config.HEADERS).json()
  for _ ,d in gist['files'].items():
    return d['content']

# Update a gist from the file in the repo, given the problem and language
def updategist(problem,language):
  gist_id = gist_id(problem,language)
  gist_contents = gist_contents(gist_id)
  file_contents = getfilecontents(problem,language)
  if (not(gist_contents == file_contents)):
    url = config.GITHUB_API + '/gists/' + str(gist_id)
    headers = config.HEADERS
    params = config.PARAMS
    filename = 'euler_problem_' + str(problem) + list(languages.keys())[list(languages.values()).index(language)]
    body = {'files':{filename:{'content':file_contents}},'public':True}

def updategists():
  return False

# if chosen_action == 1:
#   print('Updating existing gists')
#   postallgists()
# elif chosen_action == 2:
#  print('What gists do I currently have published?')
#  print(get_gists())

def main():
  print(get_gists())

if __name__ == '__main__':
  main()