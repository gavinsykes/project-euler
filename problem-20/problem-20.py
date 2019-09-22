import sys
sys.path.insert(1,'../')

import argparse
import time
from python_functions import factorial

parser = argparse.ArgumentParser(description = 'Find the sum of the digits in x!')
parser.add_argument('--num', default = 100, type = int, help = 'Insert x here, it must be a positive integer. It defaults to 100 to correspond with the Project Euler Problem at https://projecteuler.net/problem=20')
x = parser.parse_args().num

timing = {}

if ( (x < 1) and (not isinstance(x, int)) ):
    raise Exception('You entered {}, which is neither an integer nor larger than 1!'.format(x))
if (x < 1):
    raise Exception('You entered {}, which is less than 1, please try a positive integer.'.format(x))
if (not isinstance(x,int)):
    raise Exception('You entered {}, which is not an integer, please try a positive integer.'.format(x))

def euler_20(n):
    result = 0
    for i in str(factorial(n)):
        result += int(i)
    return result

timing['start'] = time.time()
result = euler_20(x)
timing['finish'] = time.time()
print(timing['start'])
print(result) # Returns 648 when x = 100
print(timing['finish'])
print('This returns {} in {} seconds!'.format(result,timing['finish']-timing['start']))
