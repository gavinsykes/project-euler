import json
import os

number_of_project_euler_problems = 736
problem_range = range(1,number_of_project_euler_problems + 1)
working_directory = os.path.dirname(__file__)
def get_languages():
    f = open('languages.json','r')
    if f.mode == 'r':
        languages = json.loads(f.read())
        return languages
extensions = list([lang['name'],lang['main']] for lang in get_languages())

def mkdirs():
  for i in problem_range:
    path = working_directory + '/problem_' + str(i)
    if not os.path.isdir(path):
      try:
        os.mkdir(path)
      except:
        print('\x1b[1;31m' + f'Creation of the directory {path} failed' + '\x1b[0m')
      else:
        print('\x1b[1;32m' + f'Creation of the directory {path} was successful!' + '\x1b[0m')
    else:
      print('\x1b[1;31m' + f'Directory {path} already exists' + '\x1b[0m')

def mkfiles():
  for i in problem_range:
    os.chdir(working_directory + '/problem_' + str(i))
    if not os.path.isfile('problem_' + str(i) + '_timings.csv'):
      try:
        file = open('problem_' + str(i) + '_timings.csv','w')
        file.close()
      except:
        print('\x1b[1;31m' + f'Creation of the timings CSV for problem {i} failed' + '\x1b[0m')
      else:
        print('\x1b[1;32m' + f'Creation of the timings CSV for problem {i} was successful!' + '\x1b[0m')
    for ext in extensions:
      if not os.path.isfile('problem_' + str(i) + ext[1]):
        try:
          file = open('problem_' + str(i) + ext[1],'w')
          file.close()
        except:
          print('\x1b[1;31m' + f'Creation of {ext[0]} file for problem {i} failed' + '\x1b[0m')
        else:
          print('\x1b[1;32m' + f'Creation of {ext[0]} file for problem {i} was successful!' + '\x1b[0m')
      else:
        print('\x1b[1;31m' + f'Problem {i} {ext[0]} file already exists' + '\x1b[0m')

def main():
  mkdirs()
  mkfiles()

if __name__ == '__main__':
  main()