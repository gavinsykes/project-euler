import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pyfuncs

challenge = 'Find the sum of all the multiples of 3 or 5 below {}:'

parser = argparse.ArgumentParser(description = 'Find the sum of all the multiples of 3 or 5 below a given number.')
parser.add_argument('--num', default = 1000, type = int, help = 'Insert the number here, it must be a positive integer. It defaults to 1000 to correspond with the Project Euler Problem at https://projecteuler.net/problem=1')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception(f'\033[1;31mYou entered {x}, which is neither an integer nor larger than 1!\033[0m')
if (x < 1):
  raise Exception(f'\033[1;31mYou entered {x}, which is less than 1, please try a positive integer.\033[0m')
if (not isinstance(x,int)):
  raise Exception(f'\033[1;31mYou entered {x}, which is not an integer, please try a positive integer.\033[0m')

def euler_1(n):
  result = 0
  x = n/3
  y = n/5

  for i in range (1,int(x)):
    result += 3*i

  for i in range (1,int(y)):
    if (5*i % 3 != 0):
      result += 5*i

  return result

pyfuncs.fullprint(challenge,euler_1,x,__file__)
