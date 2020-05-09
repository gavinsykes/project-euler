import updategists_config as config

import copy
import os
import re
import requests
import json

languages = {
  '.c':'C',
  '.cpp':'C++',
  '.java':'Java',
  '.js':'JavaScript',
  '.php':'PHP',
  '.py':'Python',
  '.rs':'Rust'
}

gists = requests.get(
  config.GITHUB_API + 'users/gavinsykes/gists',
  headers=config.HEADERS
).json()

workingdirectory = os.getcwd()

# Pull current gists
def get_gists():
  defaultdict = {'C':'No','C++':'No','Java':'No','JavaScript':'No','PHP':'No','Python':'No','Rust':'No'}
  problems = {'1':copy.copy(defaultdict)}

  for gist in gists:
    snippets = gist['files']
    for f, d in snippets.items():
      if (re.findall('euler_problem_',d['filename'])):
        if (re.findall(r'\d+',d['filename'])):
          print('re.findall function: {}'.format(re.findall(r'\d+',d['filename'])[0]))
          prob_num = re.findall(r'\d+',d['filename'])[0]
        else:
          prob_num = 0
        print('prob_num: {}'.format(prob_num))
        language = d['language']
        print('language: {}'.format(language))
        print('problems.keys(): {}'.format(problems.keys()))
        if prob_num not in problems.keys():
          problems[str(prob_num)] = copy.copy(defaultdict)
        print(problems[str(prob_num)])
        problems[str(prob_num)][language] = 'Yes'
  return problems

for problem in get_gists().items():
  print(problem)

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
    os.chdir(workingdirectory + '/problem-' + str(problem))
    ext = list(languages.keys())[list(languages.values()).index(language)]
    if (language == 'Java'):
      fi = open('problem_'+str(problem)+ext,'r')
    else:
      fi = open('problem-'+str(problem)+ext,'r')
    if fi.mode == 'r':
      return True
    else:
      return False
  except:
    return False

def getfilecontents(problem,language):
  os.chdir(workingdirectory + '/problem-' + str(problem))
  ext = list(languages.keys())[list(languages.values()).index(language)]
  if (language == 'Java'):
    fi = open('problem_'+str(problem)+ext,'r')
  else:
    fi = open('problem-'+str(problem)+ext,'r')
  if fi.mode == 'r':
    contents = fi.read()
    return contents

#getfilecontents(4,'PHP')

def getfiles():
  directorylist = list(filter(lambda dir: re.match(r'problem-',dir),os.listdir()))
  for directory in directorylist:
    os.chdir(workingdirectory + '/' + directory)
    for f in os.listdir():
      parts = os.path.splitext(f)
      if parts[1] in languages.keys():
        fi = open(f,'r')
        if fi.mode == 'r':
          contents = fi.read()
          print(contents)

# Create new gists


def postgist(url,headers,params,data):
  r = requests.post(url,headers=headers,params=params,data=data)

def creategist(problem,language):
  url = config.GITHUB_API + 'gists'
  headers = config.HEADERS
  params = config.PARAMS
  filename = 'euler_problem_' + str(problem) + list(languages.keys())[list(languages.values()).index(language)]
  body = {'files':{filename:{'content':getfilecontents(problem,language)}},'public':True}
  if (not(gistexists(problem,language))):
    postgist(url,headers,params,json.dumps(body))

def postallgists():
  for i in range(1,4):
    for l, n in languages.items():
      print('Problem ' + str(i) + ' in ' + n)
      if fileexists(i,n):
        print('\x1b[2;32;40mFile exists\x1b[0m')
        creategist(i,n)
      else:
        print('\x1b[1;31;40mFile doesn\'t exist\x1b[0m')
      if gistexists(i,n):
        print('\x1b[2;32;40mGist exists\x1b[0m')
      else:
        print('\x1b[1;31;40mGist doesn\'t exist\x1b[0m')

postallgists()

# Update existing gists

def gist_id(problem,language):
  for gist in gists:
    files = gist['files']
    for f, d in files.items():
      if (re.findall(r'\d+',d['filename'])):
        if (re.findall(r'\d+',d['filename'])[0] == str(problem)):
          if (d['language'] == language):
            return gist['id']

def gist_contents(gist_id):
  url = config.GITHUB_API + 'gists/' + str(gist_id)
  gist = requests.get(url,headers=config.HEADERS).json()
  for f ,d in gist['files'].items():
    return d['content']

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
