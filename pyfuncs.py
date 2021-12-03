from typing import Callable

def fullprint(challenge: str,fun: Callable,arg) -> None:
  import inspect
  problem_number = inspect.stack()[1][1].split('_')[-1].split('.')[0]
  import time
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
  py_v = sys.version_info
  prepare_csv_timings_file(problem_number)
  append_data_to_csv_timings_file(
    problem_number = problem_number,
    language = 'Python', 
    language_version=f'{py_v.major}.{py_v.minor}.{py_v.micro}',
    input=arg,
    time=timing['finish'] - timing['start'],
    timestamp=timing['start']
  )

def is_even(n: int) -> bool:
  return not(n & 1)

def is_odd(n: int) -> bool:
  return n & 1

def divisible_by_5(n: int) -> bool:
  return str(n)[-1] == '5' or str(n)[-1] == '0'

def is_palindrome(s) -> bool:
  if(str(s) == str(s)[::-1]):
    return True

def is_prime(n: int) -> bool:
  import math
  # Let's eliminate conditions where we can immediately see that n is not prime
  if (# n is less than 1
      n < 1 or
      # n isn't an integer
      not isinstance(n,int) or
      # n is even (unless it's 2, the only even prime number)
      (is_even(n) and n != 2) or
      # n divides by 3 (not very computationally expensive, at least I don't think so)
      n % 3 == 0 or
      # n divides by 5
      divisible_by_5(n)):
    return False

  # Okay so none of those conditions have been met but that doesn't mean it isn't prime
  # 7 is a great example of being prime but not meeting any of those conditions
  # Now for the computationally expensive bit, whittled down as much as I can
  # See at this point, only numbers that end with 1, 3, 7 or 9 can possibly be prime
  for i in range(1,int(math.floor(n/6)),1):
    if(n % (6 * i - 1) == 0 or n % (6 * i + 1) == 0):
      return False

  return True

def product_of_list(list: "list[int]") -> int:
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
