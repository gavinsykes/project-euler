from typing import Callable

def fullprint(challenge: str,fun: Callable,arg,filepath: str) -> None:
  import time
  import csv
  import os
  import json
  import sys
  from file_operations import prepare_csv_timings_file
  timing = {}
  timing['start'] = time.time()
  if arg:
    result = fun(arg)
  else:
    result = fun()
  timing['finish'] = time.time()
  print(challenge.format(arg))
  print(f'Start time: {timing["start"]}')
  print(f'Result: {result}')
  print(f'End time: {timing["finish"]}')
  print(f'This returns {result} in {timing["finish"]-timing["start"]} seconds!')
  env_file = open(os.path.dirname(__file__) + '/env_info.json','r')
  environment = json.loads(env_file.read())
  env_file.close()
  py_v = sys.version_info
  os = environment['os']
  os_release = environment['os_release']
  os_version = environment['os_version']
  machine = environment['machine']
  processor = environment['processor']
  cpu_freq = environment['cpu_freq']
  memory = environment['memory']
  prepare_csv_timings_file(filepath.split(".")[0].split("_")[2])
  with open(f'{filepath.split(".")[0]}_timings.csv', 'a', newline='') as tcsv:
    twriter = csv.writer(tcsv, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    twriter.writerow(['Python',f'{py_v.major}.{py_v.minor}.{py_v.micro}',arg,timing['finish'] - timing['start'],os,os_release,os_version,machine,processor,cpu_freq,memory,timing['start']])
    tcsv.close()

def is_even(n: int) -> bool:
  return not(n & 1)

def is_odd(n: int) -> bool:
  return n & 1

def is_palindrome(s) -> bool:
  if(str(s) == str(s)[::-1]):
    return True

def is_prime(n: int) -> bool:
  import math
  if (n < 1 or (not isinstance(n,int))):
    return None

  if((is_even(n)) or (n % 3 == 0) or (str(n)[-1:] == '5') or (str(n)[-1:] == '0')):
    return False

  for i in range(1,int(math.floor(n/6)),1):
    if(n % (6 * i - 1) == 0 or n % (6 * i + 1) == 0):
      return False

  return True

def product_of_list(list: list[int]) -> int:
  result = 1
  for i in list:
    result *= int(i)
  return result

def is_pythagorean_triple(a: int,b: int,c: int) -> bool:
  a_squared = a**2
  b_squared = b**2
  c_squared = c**2
  if (a_squared + b_squared == c_squared or a_squared + c_squared == b_squared or b_squared + c_squared == a_squared):
    return True
  return False
