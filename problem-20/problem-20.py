# n! means n x (n - 1) x ... x 3 x 2 x 1

# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def euler_20(n):
    result = 0
    for i in str(factorial(n)):
        result += int(i)
    return result

def factorial(n):
    if (type(n) != int or n < 1):
        return undefined
    if (n == 1 or n == 2):
        return n
    result = [1,2]
    for i in range(2,n,1):
        result.append((i+1) * result[i-1])
    return result[n-1]

print euler_20(100) # Returns 648
