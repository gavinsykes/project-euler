import argparse
import time

import math

parser = argparse.ArgumentParser(description = 'Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.\n\nHow many such routes are there through a nxn grid?')
parser.add_argument('--num', default = 20, type = int, help = 'Insert the number here, it must be a positive integer. It defaults to 20 to correspond with the Project Euler Problem at https://projecteuler.net/problem=15')
x = parser.parse_args().num

timing = {}

if ( (x < 1) and (not isinstance(x, int)) ):
    raise Exception('You entered {}, which is neither an integer nor larger than 1!'.format(x))
if (x < 1):
    raise Exception('You entered {}, which is less than 1, please try a positive integer.'.format(x))
if (not isinstance(x,int)):
    raise Exception('You entered {}, which is not an integer, please try a positive integer.'.format(x))

def euler_15(n):
    return nCr(2*n,n)

def nCr(n,r):
    result = 0
    if (r > n or n < 1 or r < 1):
        return undefined

    result = math.factorial(n) / (math.factorial(r) * math.factorial(n-r))
    return int(result)

timing['start'] = time.time()
result = euler_15(x)
timing['finish'] = time.time()
print('Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.\n\nHow many such routes are there through a {}x{} grid?'.format(x,x))
print('Start time: {}'.format(timing['start']))
print('Result: {}'.format(result))
print('Result: {}'.format(timing['finish']))
print('This returns {} in {} seconds!'.format(result,timing['finish']-timing['start']))
