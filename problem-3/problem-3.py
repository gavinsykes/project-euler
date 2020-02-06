import argparse
import sys

sys.path.append('/home/gavin/Documents/Git Repositories/project-euler')
import pyfuncs

challenge = 'Find the largest prime factor of {}:'

import math

parser = argparse.ArgumentParser(description = 'Find the largest prime factor of a number.')
parser.add_argument('--num', default = 600851475143, type = int, help = 'Insert the number here, it must be a positive integer. It defaults to 600851475143 to correspond with the Project Euler Problem at https://projecteuler.net/problem=3')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
    raise Exception('You entered {}, which is neither an integer nor larger than 1!'.format(x))
if (x < 1):
    raise Exception('You entered {}, which is less than 1, please try a positive integer.'.format(x))
if (not isinstance(x,int)):
    raise Exception('You entered {}, which is not an integer, please try a positive integer.'.format(x))

def gen_max_prime(n):
    if ( (n < 1) or (not isinstance(n, int)) ):
        return undefined

    while(not(n & 1)):
        result = 2
        n >>= 1

    for i in range(3,int(math.sqrt(n)) + 1,2):
        while n % i == 0:
            result = i
            n = n / i

    if n > 2:
        result = n

    return int(result)

pyfuncs.fullprint(challenge,gen_max_prime,x)
