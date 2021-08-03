import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pyfuncs

challenge = 'What is the largest prime factor of the number {}?'

parser = argparse.ArgumentParser(description = 'Find the largest prime factor of a given number.')
parser.add_argument('--num', default = 600851475143, type = int, help = 'Insert the number here, it must be a positive integer. It defaults to 600851475143 to correspond with the Project Euler Problem at https://projecteuler.net/problem=3')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception(f'\033[1;31mYou entered {x}, which is neither an integer nor larger than 1!\033[0m')
if (x < 1):
  raise Exception(f'\033[1;31mYou entered {x}, which is less than 1, please try a positive integer.\033[0m')
if (not isinstance(x,int)):
  raise Exception(f'\033[1;31mYou entered {x}, which is not an integer, please try a positive integer.\033[0m')

def euler_3(n):
  import math
  if ( (n < 1) or (not isinstance(n, int)) ):
    return None

  while(pyfuncs.is_even(n)):
    result = 2
    n >>= 1

  for i in range(3,int(math.sqrt(n)) + 1,2):
    while n % i == 0:
      result = i
      n = n / i

  if n > 2:
    result = n

  return int(result)

pyfuncs.fullprint(challenge,euler_3,x,__file__)