
def gen_max_prime(n):
  if ( (n < 1) or (not isinstance(n, int)) ):
    return undefined

  while(is_even(n)):
    result = 2
    n >>= 1

  for i in range(3,int(math.sqrt(n)) + 1,2):
    while n % i == 0:
      result = i
      n = n / i

  if n > 2:
    result = n

  return int(result)

pyfuncs.fullprint(challenge,gen_max_prime,x)
