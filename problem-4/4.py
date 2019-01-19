# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome_product(n):
    result = 0
    for i in range(n):
        for j in range(n):
            if(is_palindrome(i*j) and i*j > result):
                result = i*j
    return result

def is_palindrome(n):
    if(str(n) == str(n)[::-1]):
        return True

print largest_palindrome_product(1000) # Returns 906609
