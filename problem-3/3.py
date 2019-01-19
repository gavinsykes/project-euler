# I have decided to tackle this one in Python rather than PHP as I could quite happily do this in PHP but the point of doing these exercises is to expand my knowledge of multiple languages rather than just "solve them".
#
# Going forward it will likely be a mix of languages, I imagine it will pimarily be PHP and Python.
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

import math

def gen_max_prime(n):
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

print gen_max_prime(600851475143) # Returns 6857
