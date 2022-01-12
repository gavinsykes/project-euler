import json
from os import chdir, mkdir, path
from typing import Iterable
from file_operations import file_exists

# number_of_project_euler_problems = 736
# problem_range = range(1,number_of_project_euler_problems + 1)
# working_directory = path.dirname(__file__)
def get_languages():
    f = open('languages.json','r')
    if f.mode == 'r':
        languages = json.loads(f.read())
        return languages
extensions = [[lang['name'],lang['main']] for lang in get_languages()]

def mkdirs(problem_range: Iterable) -> None:
  for i in problem_range:
    filepath = path.dirname(__file__) + '/problem_' + str(i)
    if not path.isdir(filepath):
      try:
        mkdir(filepath)
      except:
        print('\x1b[1;31m' + f'Creation of the directory {path} failed' + '\x1b[0m')
      else:
        print('\x1b[1;32m' + f'Creation of the directory {path} was successful!' + '\x1b[0m')
    else:
      print('\x1b[1;31m' + f'Directory {path} already exists' + '\x1b[0m')

def mkfiles(problem_range: Iterable) -> None:
  for i in problem_range:
    if not file_exists(path.dirname(__file__) + f'/problem_{i}/problem_{i}_timings.csv'):
      try:
        file = open(path.dirname(__file__) + f'/problem_{i}/problem_{i}_timings.csv','w')
        file.close()
      except:
        print('\x1b[1;31m' + f'Creation of the timings CSV for problem {i} failed' + '\x1b[0m')
      else:
        print('\x1b[1;32m' + f'Creation of the timings CSV for problem {i} was successful!' + '\x1b[0m')
    for ext in extensions:
      if not file_exists(path.dirname(__file__) + f'/problem_{i}/problem_{i}{ext[1]}'):
        try:
          file = open(path.dirname(__file__) + f'/problem_{i}/problem_{i}{ext[1]}','w')
          file.close()
        except:
          print('\x1b[1;31m' + f'Creation of {ext[0]} file for problem {i} failed' + '\x1b[0m')
        else:
          print('\x1b[1;32m' + f'Creation of {ext[0]} file for problem {i} was successful!' + '\x1b[0m')
      else:
        print('\x1b[1;31m' + f'Problem {i} {ext[0]} file already exists' + '\x1b[0m')

def main():
  number_of_problems = int(input("How many Project Euler problems are there currently? "))
  problem_range = range(1,number_of_problems + 1)
  working_directory = path.dirname(__file__)

  mkdirs(problem_range)
  mkfiles(problem_range)

if __name__ == '__main__':
  main()