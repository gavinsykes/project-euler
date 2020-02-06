import argparse
import sys

sys.path.append('/home/gavin/Documents/Git Repositories/project-euler')
import pyfuncs

challenge = 'What is the {}th prime number?'

import math

parser = argparse.ArgumentParser(description = 'What is the xth prime number?')
parser.add_argument('--num', default = 10001, type = int, help = 'Insert x here, it must be a positive integer. It defaults to 10001 to correspond with the Project Euler Problem at https://projecteuler.net/problem=7')
x = parser.parse_args().num

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
        if(pyfuncs.is_prime(2 * r + 1)):
            count+=1
        r+=1
    return int(2 * r + 1)

pyfuncs.fullprint(challenge,nth_prime,x)
