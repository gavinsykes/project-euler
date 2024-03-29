from argparse import ArgumentParser
from sys import path as syspath
from os import path

syspath.append(path.dirname(path.dirname(__file__)))
from pyfuncs import fullprint, is_even

parser = ArgumentParser(description = 'Find the sum of the even-valued Fibonacci terms up to a given number.')
parser.add_argument('--num', default = 4000000, type = int, help = 'Insert the number here, it must be a positive integer. It defaults to 4000000 to correspond with the Project Euler Problem at https://projecteuler.net/problem=2')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception(f'\033[1;31mYou entered {x}, which is neither an integer nor larger than 1!\033[0m')
if (x < 1):
  raise Exception(f'\033[1;31mYou entered {x}, which is less than 1, please try a positive integer.\033[0m')
if (not isinstance(x,int)):
  raise Exception(f'\033[1;31mYou entered {x}, which is not an integer, please try a positive integer.\033[0m')

def euler_2(n):
  result = 0
  i = 1
  while (fibonacci(i) <= n):
    f = fibonacci(i)
    if is_even(f):
      result += f
    i+=1

  return result

# Function to work out the fibonacci numbers. Done as an array because it is much much faster than using a recursive function.
def fibonacci(n):
  if (not isinstance(n,int) or n < 1):
    return None # Didn't really need this as I'm controlling the input, but you just never know.

  if (n == 1 or n == 2):
    return n

  fibarray = [1,2]
  for i in range (2,n):
    fibarray.append(fibarray[i-1] + fibarray[i-2])

  return fibarray[n-1]

def main():
  challenge = f'Find the sum of the even-valued Fibonacci terms up to {x}:'
  fullprint(challenge, euler_2, x)

if __name__ == '__main__':
  main()