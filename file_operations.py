import os
import datetime
import json
import itertools

zeroth_post_date = datetime.datetime(2018,12,30,15,0,0)
workingdirectory = os.getcwd()

with open('languages.json', 'r') as im:
  langs=im.read()

languages = json.loads(langs)

language_extensions = []

for language in languages:
  language_extensions.extend(language.get('extensions'))

def file_exists(filepath):
  return os.path.isfile(filepath)

def markdown_file_exists(problem_number):
  return file_exists(workingdirectory + '/problem_' + str(problem_number) + '/problem_' + str(problem_number) + '.md')

def file_is_empty(filename):
  return os.stat(filename).st_size == 0

def markdown_file_is_empty(problem_number):
  return file_is_empty(workingdirectory + '/problem_' + str(problem_number) + '/problem_' + str(problem_number) + '.md')

def code_files_exist(problem_number):
  for key in language_extensions.keys():
    filepath = workingdirectory + '/problem_' + str(problem_number) + '/problem_' + str(key)
    if file_exists(filepath) and not file_is_empty(filepath):
      return True
  return False

def get_file_contents(filepath):
  f = open(filepath,'r')
  if f.mode == 'r':
    contents = f.read()
    return contents

def get_markdown_file_contents(problem_number):
  os.chdir(workingdirectory + '/problem_' + str(problem_number))
  fi = open('problem_' + str(problem_number) + '.md','r')
  if fi.mode == 'r':
    contents = fi.read()
    return contents
