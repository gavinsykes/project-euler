def get_file_template_python(problem_number):
    return """import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pyfuncs

challenge = ''

parser = argparse.ArgumentParser(description = '')
parser.add_argument('--num', default = ****, type = int, help = '****. It defaults to **** to correspond with the Project Euler Problem at https://projecteuler.net/problem={problem_number}')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception(f'\033[1;31mYou entered {x}, which is neither an integer nor larger than 1!\033[0m')
if (x < 1):
  raise Exception(f'\033[1;31mYou entered {x}, which is less than 1, please try a positive integer.\033[0m')
if (not isinstance(x,int)):
  raise Exception(f'\033[1;31mYou entered {x}, which is not an integer, please try a positive integer.\033[0m')

def euler_{problem_number}(n):

  return result

pyfuncs.fullprint(challenge,euler_{problem_number},x,__file__)
    """