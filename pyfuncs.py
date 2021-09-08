from typing import Callable

def fullprint(challenge: str,fun: Callable,arg,filepath: str) -> None:
  import inspect
  problem_number = inspect.stack()[1][1].split('_')[-1].split('.')[0]
  import time
  import os
  import json
  import sys
  from file_operations import prepare_csv_timings_file, append_data_to_csv_timings_file
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
  try:
    env_file = open(os.path.dirname(__file__) + '/env_info.json','r')
  except:
    raise Exception("Environment info JSON file not found, it should be in root and be called \"env_info.json\". Try running \"python3 get_env.py\" first.")
  environment = json.loads(env_file.read())
  env_file.close()
  py_v = sys.version_info
  operating_system = environment['os']
  os_release = environment['os_release']
  os_version = environment['os_version']
  machine = environment['machine']
  processor = environment['processor']
  cpu_freq = environment['cpu_freq']
  memory = environment['memory']
  prepare_csv_timings_file(problem_number)
  append_data_to_csv_timings_file(problem_number = problem_number,language = 'Python', language_version=f'{py_v.major}.{py_v.minor}.{py_v.micro}',input=arg,time=timing['finish'] - timing['start'],operating_system=operating_system,os_release=os_release,os_version=os_version,machine=machine,processor=processor,cpu_freq=cpu_freq,memory=memory,timestamp=timing['start'])

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
