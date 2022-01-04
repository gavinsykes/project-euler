from typing import Callable

def check_correct_answer(problem_number: int, input: int, fun: Callable) -> bool:
  from json import loads
  with open(f'problem_{problem_number}/problem_{problem_number}_expected_answers.json','r') as expected_answers_file:
    expected_answers_data = expected_answers_file.read()
    expected_answers = loads(expected_answers_data)
  try:
    expected_answer = list(filter(lambda answer: answer["input"] == input, expected_answers))[0]["expected_answer"]
  except IndexError:
    return None
  return expected_answer == fun(input)

def fullprint(challenge: str,fun: Callable,arg) -> None:
  from inspect import stack
  from time import time, perf_counter
  from sys import version_info
  from file_operations import prepare_csv_timings_file, append_data_to_csv_timings_file

  problem_number = stack()[1][1].split('_')[-1].split('.')[0]
  timing = {}
  timestamp = time()
  timing['start'] = perf_counter()
  if arg:
    result = fun(arg)
  else:
    result = fun()
  timing['finish'] = perf_counter()
  print(challenge.format(arg))
  print(f'This returns {result} in {timing["finish"]-timing["start"]} seconds!')
  if check_correct_answer(problem_number, arg, fun) is None:
    print('\033[1;33mWARNING: this input has not yet been given an expected answer, please consider giving it one.')
    print('For now I will avoid adding the answer to the CSV. Exiting...\033[0m')
    return
  if check_correct_answer(problem_number, arg, fun):
    print('\033[1;32mAnswer appears to be correct, adding data to the CSV...')
    py_v = version_info
    prepare_csv_timings_file(problem_number)
    append_data_to_csv_timings_file(
      problem_number = problem_number,
      language = 'Python', 
      language_version=f'{py_v.major}.{py_v.minor}.{py_v.micro}',
      input=arg,
      time=timing['finish'] - timing['start'],
      timestamp=timestamp
    )
    print('Exiting...\033[0m')
  else:
    print(f'\033[1;31mERROR: Answer appears to be wrong, {result} given. Exiting...\033[0m')

def is_even(n: int) -> bool:
  return not(n & 1)

def is_odd(n: int) -> bool:
  return n & 1

def divisible_by_5(n: int) -> bool:
  return str(n)[-1] == '5' or str(n)[-1] == '0'

def is_palindrome(s: any) -> bool:
  if(str(s) == str(s)[::-1]):
    return True

def is_prime(n: int) -> bool:  # Let's eliminate conditions where we can immediately see that n is not prime
  if (# n is less than 1
      n < 1 or
      # n isn't an integer
      not isinstance(n,int) or
      # n is even (unless it's 2, the only even prime number)
      (is_even(n) and n != 2) or
      # n divides by 3 (not very computationally expensive, at least I don't think so)
      # Remember this doesn't actually include 3!
      (n % 3 == 0 and n != 3) or
      # n divides by 5
      # Nor does this include 5 itself!
      (divisible_by_5(n) and n != 5)):
    print(f'{n} met one of the basic conditions, not prime')
    return False

  # Okay so none of those conditions have been met but that doesn't mean it isn't prime.
  # 7 is a great example of being prime but not meeting any of those conditions.
  # Now for the computationally expensive bit, whittled down as much as I can.
  # See at this point, only numbers that end with 1, 3, 7 or 9 can possibly be prime.
  # We have already eliminated 1, 3, and 5, so we have to start at 7 and pick up every odd number
  # Mathematically, with m starting at 1, that is 2m+5 where 2m+5 < n meaning m < (n-5)/2
  # We also need to take out every 5th iteration of m, as they will be multiples of 5 which we have already handled
  m = 1
  c5 = 1
  while m < (n-5)/2:
    # If we are on a 5th number, set the "multiple of 5 counter" back to 1 and skip this loop
    if c5 == 5:
      c5 = 1
      continue
    if (n % (2*m + 5) == 0):
      return False
    m+=1
    c5+=1

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

if __name__ == '__main__':
  print(check_correct_answer(1,1001))