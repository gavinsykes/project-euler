import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pyfuncs

challenge = 'Find the difference between the sum of the squares of the first {} natural numbers and the square of the sum:'

parser = argparse.ArgumentParser(description = 'Find the difference between the sum of the squares of the first x natural numbers and the square of the sum.')
parser.add_argument('--num', default = 10, type = int, help = 'Insert the number here, it must be a positive integer. It defaults to 10 to correspond with the Project Euler Problem at https://projecteuler.net/problem=6')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception(f'You entered {x}, which is neither an integer nor larger than 1!')
if (x < 1):
  raise Exception(f'You entered {x}, which is less than 1, please try a positive integer.')
if (not isinstance(x,int)):
  raise Exception(f'You entered {x}, which is not an integer, please try a positive integer.')

def euler_6(n):
  if ( (n < 1) or (not isinstance(n, int)) ):
    return None

  result = 0
  sumsquares = 0
  _sum = 0
  squaresum = 0
  for i in range(n):
    sumsquares += i ** 2
  for i in range(n):
    _sum += i
  squaresum = _sum ** 2
  result = squaresum - sumsquares
  return result

pyfuncs.fullprint(challenge,euler_6,x,__file__)
