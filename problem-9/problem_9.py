import sys

sys.path.append('/home/gavin/project-euler')
import pyfuncs

challenge = 'There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.'

def euler_9(n):
  a = b = c = 1;
  for a in range(1,n-2):
    for b in range(1,n-a-1):
      c = n - a - b;
      if (pyfuncs.is_pythagorean_triple(a,b,c)):
        return(f'{a}, {b} and {c} make {a*b*c}')

pyfuncs.fullprint(challenge,euler_9,1000)
