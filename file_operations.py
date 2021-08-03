import os
import datetime
import json

zeroth_post_date = datetime.datetime(2018,12,30,15,0,0)
workingdirectory = os.getcwd()
this_directory = os.path.dirname(__file__)

def csv_timings_file_exists(problem_number: int) -> bool:
  print(this_directory + '/problem_' + str(problem_number) + '/problem_' + str(problem_number) + '_timings.csv')
  return file_exists(this_directory + '/problem_' + str(problem_number) + '/problem_' + str(problem_number) + '_timings.csv')

def csv_timings_file_prepared(problem_number: int) -> bool:
  print('Checking if CSV file for problem {} is prepared.'.format(problem_number))
  if not csv_timings_file_exists(problem_number):
    print('It doesn\'t exist.')
    return False
  import csv
  with open(this_directory + '/problem_' + str(problem_number) + '/problem_' + str(problem_number) + '_timings.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    row1 = next(reader)
    if row1[0] == 'language':
      print('It\'s prepared')
      return True
    print('It isn\'t prepared')
    return False

def csv_timings_file_is_empty(problem_number: int) -> bool:
  return file_is_empty(this_directory + '/problem_' + str(problem_number) + '/problem_' + str(problem_number) + '_timings.csv')

def prepare_csv_timings_file(problem_number: int) -> None:
  if csv_timings_file_prepared(problem_number):
    print('No need to continue')
    return
  if not csv_timings_file_is_empty(problem_number):
    raise Exception('The CSV timings file for problem {} isn\'t prepared, but also doesn\'t appear to be empty. Manual intervention required.'.format(str(problem_number)))
  import csv
  with open(this_directory + '/problem_' + str(problem_number) + '/problem_' + str(problem_number) + '_timings.csv', 'w', newline='') as csv_file:
      writer = csv.writer(csv_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
      writer.writerow(['language', 'language_version', 'input', 'time', 'os', 'os_release', 'os_version', 'machine', 'processor', 'cpu_freq', 'memory', 'timestamp'])

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
  if file_exists(filename):
    return os.stat(filename).st_size == 0
  return False

def markdown_file_is_empty(problem_number):
  return file_is_empty(workingdirectory + '/problem_' + str(problem_number) + '/problem_' + str(problem_number) + '.md')

def code_files_exist(problem_number):
  for key in language_extensions.keys():
    filepath = workingdirectory + '/problem_' + str(problem_number) + '/problem_' + str(problem_number) + str(key)
    if file_exists(filepath) and not file_is_empty(filepath):
      return True
  return False

def code_file_exists(problem_number,language):
  for extension in list(l['extensions'] for l in languages if l['name'] == language)[0]:
    filepath = workingdirectory + '/problem_' + str(problem_number) + '/problem_' + str(problem_number) + str(extension)
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

def main():
  return None

if __name__ == '__main__':
  main()