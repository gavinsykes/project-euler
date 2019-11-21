import argparse
import time

parser = argparse.ArgumentParser(description = 'Find the sum of all the multiples of 3 or 5 below a given number.')
parser.add_argument('--num', default = 1000, type = int, help = 'Insert the number here, it must be a positive integer. It defaults to 1000 to correspond with the Project Euler Problem at https://projecteuler.net/problem=1')
x = parser.parse_args().num

timing = {}

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception('You entered {}, which is neither an integer nor larger than 1!'.format(x))
if (x < 1):
  raise Exception('You entered {}, which is less than 1, please try a positive integer.'.format(x))
if (not isinstance(x,int)):
  raise Exception('You entered {}, which is not an integer, please try a positive integer.'.format(x))

def euler_1(n):
    result = 0
    x = n/3
    y = n/5

    for i in range (1,int(x)):
        result += 3*i

    for i in range (1,int(y)):
        if (5*i % 3 != 0):
            result += 5*i

    return result

timing['start'] = time.time()
result = euler_1(x)
timing['finish'] = time.time()
print(timing['start'])
print(result) # Returns 232169 when x = 1000
print(timing['finish'])
print('This returns {} in {} seconds!'.format(result,timing['finish']-timing['start']))
