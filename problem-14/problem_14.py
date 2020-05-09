import argparse
import sys

sys.path.append('/home/gavin/project-euler')
import pyfuncs

challenge = 'Which starting number, under {}, produces the longest chain in the Collatz problem?'

parser = argparse.ArgumentParser(description = 'Which starting number, under x, produces the longest chain in the Collatz problem?')
parser.add_argument('--num', default = 500, type = int, help = 'Insert the number here, it must be a positive integer. It defaults to 1000000 to correspond with the Project Euler Problem at https://projecteuler.net/problem=14')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception(f'You entered {x}, which is neither an integer nor larger than 1!')
if (x < 1):
  raise Exception(f'You entered {x}, which is less than 1, please try a positive integer.')
if (not isinstance(x,int)):
  raise Exception(f'You entered {x}, which is not an integer, please try a positive integer.')

def euler_14(n):
  longest = 0
  num = 0
  for i in range (1,n):
    new_l = len(collatz_sequence(i))
    if (new_l > longest):
      longest = new_l
      num = i

def collatz_sequence(n):
  res = list()
  curr = n
  while (next_step(curr) != 1):
    res.append(curr)
    curr = next_step(curr)
  return res

def next_step(n):
  if (pyfuncs.is_even(n)):
    return int(n / 2)
  if (pyfuncs.is_odd(n)):
    return int(3 * n + 1)

pyfuncs.fullprint(challenge,euler_14,x)
