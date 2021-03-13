import argparse
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))
import pyfuncs

challenge = 'In this variation of Secret Santa each of the n people gives and receives two presents. At the beginning each of the people writes their name on two slips of paper and puts the slips into a hat (there will be 2n slips of paper in the hat). As before each person takes from the hat a random slip that does not contain their own name. Then the same person repeats this process thus ending up with two slips, neither of which contains that person\'s own name. Then the next person draws two slips in the same way, and so on. The process will fail if the last person gets at least one slip with their own name. Define q(n) to be the probabilty of this happening. Find q(n) to 10 decimal places.'

parser = argparse.ArgumentParser(description = '')
parser.add_argument('--num', default = 100, type = int, help = 'Insert the number here, it must be a positive integer. It defaults to 100 to correspond with the Project Euler Problem at https://projecteuler.net/problem=735')
x = parser.parse_args().num

if ( (x < 1) and (not isinstance(x, int)) ):
  raise Exception(f'You entered {x}, which is neither an integer nor larger than 1!')
if (x < 1):
  raise Exception(f'You entered {x}, which is less than 1, please try a positive integer.')
if (not isinstance(x,int)):
  raise Exception(f'You entered {x}, which is not an integer, please try a positive integer.')

def euler_735(n):
  from functools import reduce
  probabilities = [1/n]
  non_probabilities = [1 - 1/n]
  def only_one_happened(li1,li2):
    result = 0
    for index,value in enumerate(li1):
      copy_li2 = li2.copy()
      del copy_li2[index]
      result += value * sum(copy_li2)
    return result
  for i in range (0,2*n):
    probability = only_one_happened(probabilities,non_probabilities) * (1/(2*n-i)) + pyfuncs.prod(non_probabilities) * (2/(2*n-i))
    probabilities.append(probability)
    non_probabilities.append(1-probability)
  return only_one_happened(probabilities[0:2*n-2],non_probabilities[0:2*n-2]) + sum(non_probabilities[0:2*n-2])

pyfuncs.fullprint(challenge,euler_735,x)
