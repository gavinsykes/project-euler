import argparse
import sys

sys.path.append('/home/gavin/Documents/Git Repositories/project-euler')
import pyfuncs

challenge = 'Find the largest palindrome made from the product of 2 numbers of {} digits:'

parser = argparse.ArgumentParser(description = 'Find the largest palindrome made from the product of 2 numbers of x digits.')
parser.add_argument('--num', default = 3, type = int, help = 'Insert the number of digits here, it must be a positive integer. It defaults to 3 to correspond with the Project Euler Problem at https://projecteuler.net/problem=4')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
    raise Exception('You entered {}, which is neither an integer nor larger than 1!'.format(x))
if (x < 1):
    raise Exception('You entered {}, which is less than 1, please try a positive integer.'.format(x))
if (not isinstance(x,int)):
    raise Exception('You entered {}, which is not an integer, please try a positive integer.'.format(x))

def largest_palindrome_product(n):
    if ( (n < 1) or (not isinstance(n, int)) ):
        return undefined

    result = 0
    for i in range(10**n):
        for j in range(10**n):
            if(pyfuncs.is_palindrome(i*j) and i*j > result):
                result = i*j
    return result

pyfuncs.fullprint(challenge,largest_palindrome_product,x)
