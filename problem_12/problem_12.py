import argparse
import sys

sys.path.append('/home/gavin/project-euler')
import pyfuncs

challenge = 'What is the value of the first triangle number to have over {} divisors?'

parser = argparse.ArgumentParser(description = 'What is the value of the first triangle number to have over x divisors?')
parser.add_argument('--num', default = 500, type = int, help = 'Insert the number here, it must be a positive integer. It defaults to 500 to correspond with the Project Euler Problem at https://projecteuler.net/problem=12')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception(f'You entered {x}, which is neither an integer nor larger than 1!')
if (x < 1):
  raise Exception(f'You entered {x}, which is less than 1, please try a positive integer.')
if (not isinstance(x,int)):
  raise Exception(f'You entered {x}, which is not an integer, please try a positive integer.')

def euler_12(n):
  i = 1
  while (len(get_divisors(i)) < n + 1):
    i += 1
  return i

def get_divisors(n):
  divisors = list()
  if (not isinstance(n,int) or n < 1):
    return undefined

  for i in range(1,int(n/2)):
    if (n % i == 0):
      divisors.append(i)
      divisors.append(int(n/i))

  l = list(dict.fromkeys(divisors))
  l.sort()
  return l

pyfuncs.fullprint(challenge,euler_12,x)
