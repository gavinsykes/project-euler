# I have decided to tackle this one in Python rather than PHP as I could quite happily do this in PHP but the point of doing these exercises is to expand my knowledge of multiple languages rather than just "solve them".

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def euler_6(n):
    result = 0
    sumsquares = 0
    _sum = 0
    squaresum = 0
    for i in range(n):
        sumsquares += i ** 2
    for i in range(n):
        _sum += i
    squaresum = _sum ** 2
    result = squaresum - sumsquares
    return result

print euler_6(100)
