def factorial(n):
    if (n < 1 or (not isinstance(n,int))):
        return undefined
    if (n == 1 or n == 2):
        return n
    result = [1,2]
    for i in range(2,n,1):
        result.append((i+1) * result[i-1])
    return result[n-1]

def is_palindrome(s):
    if(str(s) == str(s)[::-1]):
        return True

def is_prime(n):
    if (n < 1 or (not isinstance(n,int))):
        return undefined

    if(not(n & 1)):
        return False

    if(n % 3 == 0):
        return False

    if((str(n)[-1:] == '5') or (str(n)[-1:] == '0')):
        return False

    for i in range(1,int(math.floor(n/6)),1):
        if(n % (6 * i - 1) == 0 or n % (6 * i + 1) == 0):
            return False

    return True

def prod(li):
    result = 1
    for i in li:
        result *= int(i)
    return result
