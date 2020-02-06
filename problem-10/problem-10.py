import argparse
import sys

sys.path.append('/home/gavin/Documents/Git Repositories/project-euler')
import pyfuncs

challenge = 'Find the sum of all the primes below {}:'

import math

parser = argparse.ArgumentParser(description = 'Find the sum of all the primes below x')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
    raise Exception('You entered {}, which is neither an integer nor larger than 1!'.format(x))
if (x < 1):
    raise Exception('You entered {}, which is less than 1, please try a positive integer.'.format(x))
if (not isinstance(x,int)):
    raise Exception('You entered {}, which is not an integer, please try a positive integer.'.format(x))

def is_prime(n):
    # Check if it's divisible by 2
    if(not(n & 1)):
        return False
    
    # If we've got this far then only a certain subset of numbers are eligible to be prime, which, after 5, is the first 2 of every 3 odd numbers.
    # First let's check if our number is divisible by either 3 or 5.
    if(n % 3 == 0):
        return False
    
    if((str(n)[-1:] == '5') or (str(n)[-1:] == '0')):
        return False
    
    for i in range(1,int(math.floor(n/6)),1):
        if(n % (6 * i - 1) == 0 or n % (6 * i + 1) == 0):
            return False
    
    # If we've got this far then our number must be prime
    return True

def euler_10(n):
    result = 0
    for i in range(1,n):
        if is_prime(i):
            result += i
    return result

pyfuncs.fullprint(challenge,euler_10,x)

# Need to find a faster way to do this, I started it running at the 65-minute mark of Chelsea vs Burnley and checked back just after they'd had the post-match interview with Sean Dyche, and it still hadn't calculated!
