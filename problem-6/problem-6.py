import argparse
import time

parser = argparse.ArgumentParser(description = 'Find the difference between the sum of the squares of the first x natural numbers and the square of the sum.')
parser.add_argument('--num', default = 10, type = int, help = 'Insert the number here, it must be a positive integer. It defaults to 10 to correspond with the Project Euler Problem at https://projecteuler.net/problem=6')
x = parser.parse_args().num

timing = {}

if ( (x < 1) and (not isinstance(x, int)) ):
    raise Exception('You entered {}, which is neither an integer nor larger than 1!'.format(x))
if (x < 1):
    raise Exception('You entered {}, which is less than 1, please try a positive integer.'.format(x))
if (not isinstance(x,int)):
    raise Exception('You entered {}, which is not an integer, please try a positive integer.'.format(x))

def euler_6(n):
    if ( (n < 1) or (not isinstance(n, int)) ):
        return undefined

    result = 0
    sumsquares = 0
    _sum = 0
    squaresum = 0
    for i in range(n):
        sumsquares += i ** 2
    for i in range(n):
        _sum += i
    squaresum = _sum ** 2
    result = squaresum - sumsquares
    return result

timing['start'] = time.time()
result = euler_6(x)
timing['finish'] = time.time()
print('Find the difference between the sum of the squares of the first {} natural numbers and the square of the sum.'.format(x))
print('Start time: {}'.format(timing['start']))
print('Result: {}'.format(result)) # Returns 24174150 when x = 100
print('End time: {}'.format(timing['finish']))
print('This returns {} in {} seconds!'.format(result,timing['finish']-timing['start']))
