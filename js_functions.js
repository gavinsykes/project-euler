export const is_even = n => !n&1;
export const is_odd = n => n&1;

export const is_palindrome = n => n.toString().split('').every((c,i) => c === n.toString().split('').reverse()[i]);

export const productOfArray = array => array.reduce((accumulator,current) => current * accumulator,1);

export const is_pythagorean_triple = (a,b,c) => (a**2+b**2==c**2 || a**2+c**2==b**2 || b**2+c**2==a**2);

export const fullprint = (challenge,fun,argument,filepath) => {
  const timing = {};
  result = argument ? fun(argument) : fun();
  console.log(challenge);
}

/* The below is to be converted from Python

def fullprint(challenge,fun,arg,filepath):
  import time
  import csv
  import platform
  import psutil
  import os
  import sys
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
  uname = platform.uname()
  cpu = psutil.cpu_freq()
  mem = psutil.virtual_memory()
  with open(f'{filepath.split(".")[0]}_timings.csv', 'a', newline='') as tcsv:
    twriter = csv.writer(tcsv, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    twriter.writerow(['Python',f'{py_v.major}.{py_v.minor}.{py_v.micro}',arg,timing['finish'] - timing['start'],uname.system,uname.release,uname.version,uname.machine,uname.processor,cpu.current,mem.total,timing['start']])
    tcsv.close()

def is_palindrome(s):
  if(str(s) == str(s)[::-1]):
    return True

def is_prime(n):
  import math
  if (n < 1 or (not isinstance(n,int))):
    return None

  if((is_even(n)) or (n % 3 == 0) or (str(n)[-1:] == '5') or (str(n)[-1:] == '0')):
    return False

  for i in range(1,int(math.floor(n/6)),1):
    if(n % (6 * i - 1) == 0 or n % (6 * i + 1) == 0):
      return False

  return True */