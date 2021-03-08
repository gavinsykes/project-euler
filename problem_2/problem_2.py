import argparse
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
import pyfuncs

challenge = 'Find the sum of the even-valued Fibonacci terms up to {}:'

parser = argparse.ArgumentParser(description = 'Find the sum of the even-valued Fibonacci terms up to a given number.')
parser.add_argument('--num', default = 4000000, type = int, help = 'Insert the number here, it must be a positive integer. It defaults to 4000000 to correspond with the Project Euler Problem at https://projecteuler.net/problem=2')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception(f'You entered {x}, which is neither an integer nor larger than 1!')
if (x < 1):
  raise Exception(f'You entered {x}, which is less than 1, please try a positive integer.')
if (not isinstance(x,int)):
  raise Exception(f'You entered {x}, which is not an integer, please try a positive integer.')

def euler_2(n):
  result = 0
  i = 1
  while (fibonacci(i) < n):
    i+=1
    f = fibonacci(i)
    if (not(f & 1)):
      result += f

  return result

# Function to work out the fibonacci numbers. Done as an array because it is much much faster than using a recursive function.
def fibonacci(n):
  if (not isinstance(n,int) or n < 1):
    return undefined # Didn't really need this as I'm controlling the input, but you just never know.

  if (n == 1 or n == 2):
    return n

  fibarray = [1,2]
  for i in range (2,n):
    fibarray.append(fibarray[i-1] + fibarray[i-2])

  return fibarray[n-1]

pyfuncs.fullprint(challenge,euler_2,x)
