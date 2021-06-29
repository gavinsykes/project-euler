import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pyfuncs

challenge = ''

parser = argparse.ArgumentParser(description = '')
parser.add_argument('--num', default = 1000, type = int, help = '')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception(f'\033[1;31mYou entered {x}, which is neither an integer nor larger than 1!\033[0m')
if (x < 1):
  raise Exception(f'\033[1;31mYou entered {x}, which is less than 1, please try a positive integer.\033[0m')
if (not isinstance(x,int)):
  raise Exception(f'\033[1;31mYou entered {x}, which is not an integer, please try a positive integer.\033[0m')

###
### Code goes here
###

pyfuncs.fullprint(challenge,function_name,x,__file__)
