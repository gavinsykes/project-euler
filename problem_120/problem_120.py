import argparse
import sys

sys.path.append('/home/gavin/project-euler')
import pyfuncs

challenge = 'Let r be the remainder when (a-1)^n + (a+1)^n is divided by a^2.\n\nFor example, if a=7 and n=3, then r=42: 6^3 + 8^3 = 728 = 42 mod 49. And as n varies, so too will r, but for a=7 it turns out that r_max = 42.\n\nFor 3 <= a <= {}, find SUM(r_max)'

parser = argparse.ArgumentParser(description = 'Let r be the remainder when (a-1)^n + (a+1)^n is divided by a^2.\n\nFor example, if a=7 and n=3, then r=42: 6^3 + 8^3 = 728 = 42 mod 49. And as n varies, so too will r, but for a=7 it turns out that r_max = 42.\n\nFor 3 <= a <= x, find SUM(r_max)')
parser.add_argument('--num', default = 1000, type = int, help = 'Insert the number here, it must be a positive integer. It defaults to 1000 to correspond with the Project Euler Problem at https://projecteuler.net/problem=120')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception(f'You entered {x}, which is neither an integer nor larger than 1!')
if (x < 1):
  raise Exception(f'You entered {x}, which is less than 1, please try a positive integer.')
if (not isinstance(x,int)):
  raise Exception(f'You entered {x}, which is not an integer, please try a positive integer.')

def euler_120(n):
  result = n
  return result

pyfuncs.fullprint(challenge,euler_120,x)
