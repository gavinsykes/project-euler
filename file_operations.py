import os
import datetime

zeroth_post_date = datetime.datetime(2018,12,30,15,0,0)
workingdirectory = os.getcwd()

language_extensions = {'.c':'C',
                       '.cpp':'C++',
                       '.java':'Java',
                       '.js':'JavaScript',
                       '.php':'PHP',
                       '.py':'Python',
                       '.rs':'Rust',
                       '.ts':'TypeScript'
                      }

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

def get_file_contents(number):
  os.chdir(workingdirectory + '/problem_' + str(number))
  fi = open('problem_' + str(number) + '.md','r')
  if fi.mode == 'r':
    contents = fi.read()
    return contents
