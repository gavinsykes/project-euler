from os import chdir, getcwd, path, stat
from datetime import datetime
from json import loads
from argparse import ArgumentParser
from csv import reader as csv_reader, writer as csv_writer, QUOTE_MINIMAL

zeroth_post_date = datetime(2018,12,30,15,0,0)
workingdirectory = getcwd()
this_directory = path.dirname(__file__)

def csv_timings_file_exists(problem_number: int) -> bool:
  return file_exists(this_directory + f'/problem_{problem_number}/problem_{problem_number}_timings.csv')

def csv_timings_file_prepared(problem_number: int) -> bool:
  if not csv_timings_file_exists(problem_number):
    return False
  with open(this_directory + f'/problem_{problem_number}/problem_{problem_number}_timings.csv', newline='') as csv_file:
    reader = csv_reader(csv_file)
    row1 = next(reader)
    if row1[0] == 'language':
      return True
    return False

def csv_timings_file_is_empty(problem_number: int) -> bool:
  return file_is_empty(this_directory + f'/problem_{problem_number}/problem_{problem_number}_timings.csv')

def prepare_csv_timings_file(problem_number: int) -> None:
  if csv_timings_file_exists(problem_number):
    if not csv_timings_file_is_empty(problem_number):
      if csv_timings_file_prepared(problem_number):
        return
      else:
        raise Exception(f'The CSV timings file for problem {problem_number} isn\'t prepared, but also doesn\'t appear to be empty. Manual intervention required.')
  with open(this_directory + f'/problem_{problem_number}/problem_{problem_number}_timings.csv', 'w', newline='') as csv_file:
      writer = csv_writer(csv_file, delimiter = ',', quotechar = '"', quoting = QUOTE_MINIMAL)
      writer.writerow(['language', 'language_version', 'input', 'time', 'os', 'os_release', 'os_version', 'machine', 'processor', 'cpu_freq', 'memory', 'timestamp'])

def append_data_to_csv_timings_file(
  problem_number: int,
  language: str,
  language_version: str,
  input: int,
  time: float,
  timestamp: float
) -> None:
  prepare_csv_timings_file(problem_number)
  try:
    env_file = open(path.dirname(__file__) + '/env_info.json','r')
  except:
    raise Exception("\x1b[1;31mEnvironment info JSON file not found, it should be in root and be called \"env_info.json\". Try running \"python3 get_env.py\" first.\x1b[0m")
  environment = loads(env_file.read())
  env_file.close()
  operating_system = environment['os']
  os_release = environment['os_release']
  os_version = environment['os_version']
  machine = environment['machine']
  processor = environment['processor']
  cpu_freq = environment['cpu_freq']
  memory = environment['memory']
  with open(this_directory + f'/problem_{problem_number}/problem_{problem_number}_timings.csv', 'a', newline='') as csv_file:
      writer = csv_writer(csv_file, delimiter = ',', quotechar = '"', quoting = QUOTE_MINIMAL)
      writer.writerow([language,language_version,input,time,operating_system,os_release,os_version,machine,processor,cpu_freq,memory,timestamp])

with open('languages.json', 'r') as im:
  langs=im.read()

languages = loads(langs)

language_extensions = []

for language in languages:
  language_extensions.extend(language.get('extensions'))

def file_exists(filepath):
  return path.isfile(filepath)

def markdown_file_exists(problem_number):
  return file_exists(workingdirectory + f'/problem_{problem_number}/problem_{problem_number}.md')

def file_is_empty(filename):
  if file_exists(filename):
    return stat(filename).st_size == 0
  return False

def markdown_file_is_empty(problem_number):
  return file_is_empty(workingdirectory + f'/problem_{problem_number}/problem_{problem_number}.md')

def code_files_exist(problem_number):
  for key in language_extensions.keys():
    filepath = workingdirectory + f'/problem_{problem_number}/problem_{problem_number}{key}'
    if file_exists(filepath) and not file_is_empty(filepath):
      return True
  return False

def code_file_exists(problem_number,language):
  for extension in list(l['extensions'] for l in languages if l['name'] == language)[0]:
    filepath = workingdirectory + f'/problem_{problem_number}/problem_{problem_number}{extension}'
    if file_exists(filepath) and not file_is_empty(filepath):
      return True
  return False

def get_file_contents(filepath):
  with open(filepath,'r') as file:
    return file.read()

def get_markdown_file_contents(problem_number):
  filepath = this_directory + f'/problem_{problem_number}/problem_{problem_number}.md'
  return get_file_contents(filepath)

def main():
  parser = ArgumentParser(description = 'This file contains all of the necessary file operations to keep this repository operating.')
  parser.add_argument('-c', '--csv', action = "store_true", help = 'Set this option to tell the program you are updating the CSV')
  parser.add_argument('-n', '--problem_number', type = int, help = 'The number of the problem that you wish to update')
  parser.add_argument('-i', '--input', type = int, help = 'The input provided to the function for solving the problem')
  parser.add_argument('-l', '--language', help = 'The language the problem has been completed in')
  parser.add_argument('-g', '--language_version', help = 'The version of the language')
  parser.add_argument('-t', '--time', type = float, help = 'The time taken to solve the problem')
  parser.add_argument('-s', '--timestamp', type = float, help = 'The time that the function was run')
  args = parser.parse_args()
  if args.csv:
    if None not in vars(args).values():
      append_data_to_csv_timings_file(
        problem_number   = args.problem_number,
        language         = args.language,
        language_version = args.language_version,
        input            = args.input,
        time             = args.time,
        timestamp        = args.timestamp
      )
  return None

if __name__ == '__main__':
  print(get_markdown_file_contents(1))
  # main()