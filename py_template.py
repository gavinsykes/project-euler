import argparse
import sys

sys.path.append('/home/gavin/project-euler')
import pyfuncs

challenge = ''

parser = argparse.ArgumentParser(description = '')
parser.add_argument('--num', default = 1000, type = int, help = '')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception(f'You entered {x}, which is neither an integer nor larger than 1!')
if (x < 1):
  raise Exception(f'You entered {x}, which is less than 1, please try a positive integer.')
if (not isinstance(x,int)):
  raise Exception(f'You entered {x}, which is not an integer, please try a positive integer.')

###
### Code goes here
###

pyfuncs.fullprint(challenge,euler_1,x)
