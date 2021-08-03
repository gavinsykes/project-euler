import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pyfuncs

challenge = 'Find the largest palindrome made from the product of 2 numbers of {} digits:'

parser = argparse.ArgumentParser(description = 'Find the largest palindrome made from the product of 2 numbers of x digits.')
parser.add_argument('--num', default = 3, type = int, help = 'Insert the number of digits here, it must be a positive integer. It defaults to 3 to correspond with the Project Euler Problem at https://projecteuler.net/problem=4')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception(f'You entered {x}, which is neither an integer nor larger than 1!')
if (x < 1):
  raise Exception(f'You entered {x}, which is less than 1, please try a positive integer.')
if (not isinstance(x,int)):
  raise Exception(f'You entered {x}, which is not an integer, please try a positive integer.')

def euler_4(n):
    if ( (n < 1) or (not isinstance(n, int)) ):
        return None

    result = 0
    for i in range(10**n):
        for j in range(10**n):
            if(pyfuncs.is_palindrome(i*j) and i*j > result):
                result = i*j
    return result

pyfuncs.fullprint(challenge,euler_4,x,__file__)
