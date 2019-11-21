import sys
sys.path.insert(1,'../')

import time
import argparse
from python_functions import is_prime

import math

parser = argparse.ArgumentParser(description = 'What is the xth prime number?')
parser.add_argument('--num', default = 10001, type = int, help = 'Insert x here, it must be a positive integer. It defaults to 10001 to correspond with the Project Euler Problem at https://projecteuler.net/problem=7')
x = parser.parse_args().num

timing = {}

if ( (x < 1) and (not isinstance(x, int)) ):
    raise Exception('You entered {}, which is neither an integer nor larger than 1!'.format(x))
if (x < 1):
    raise Exception('You entered {}, which is less than 1, please try a positive integer.'.format(x))
if (not isinstance(x,int)):
    raise Exception('You entered {}, which is not an integer, please try a positive integer.'.format(x))

def nth_prime(n):
    r = 0
    count = 1
    while(count<=n):
        if(is_prime(2 * r + 1)):
            count+=1
        r+=1
    return int(2 * r + 1)

timing['start'] = time.time()
result = nth_prime(x)
timing['finish'] = time.time()
print(timing['start'])
print(result) # Returns 104763 when x = 10001
print(timing['finish'])
print('This returns {} in {} seconds!'.format(result,timing['finish']-timing['start']))
