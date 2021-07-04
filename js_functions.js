const fs = require('fs');

export const is_even = n => !n&1;
export const is_odd = n => n&1;

export const is_palindrome = n => n.toString().split('').every((c,i) => c === n.toString().split('').reverse()[i]);

export const productOfArray = array => array.reduce((accumulator,current) => current * accumulator,1);

export const is_pythagorean_triple = (a,b,c) => (a**2+b**2==c**2 || a**2+c**2==b**2 || b**2+c**2==a**2);

export const fullprint = (challenge,fun,argument,filepath) => {
  const timing = {};
  timing.start = Date.now();
  result = argument ? fun(argument) : fun();
  timing.finish = Date.now();
  console.log(`Start time: ${timing.start}`);
  console.log(`Result: ${result}`);
  console.log(`Finish time: ${timing.finish}`);
  console.log(`This returns ${result} in ${timing.finish - timing.start} seconds!`);
  node_v = process.versions.v8.split('.');
  fs.writeFile(
    'problem_1/problem_1_timings.csv',
    [
      'JavaScript',
      `${node_v[0]}.${node_v[1]}.${node_v[2]}`,
      arg,
      timing['finish'] - timing['start'],
      "Windows",
      10,
      "10.0.19042",
      "AMD64",
      "Intel64 Family 6 Model 126 Stepping 5, GenuineIntel",
      991.0,
      8356937728,
      timing.start
    ].join(','),
    {
      encoding:'utf8',
      flag:'a'
    },error => console.log(error));
}

/* The below is to be converted from Python

def is_prime(n):
  import math
  if (n < 1 or (not isinstance(n,int))):
    return None

  if((is_even(n)) or (n % 3 == 0) or (str(n)[-1:] == '5') or (str(n)[-1:] == '0')):
    return False

  for i in range(1,int(math.floor(n/6)),1):
    if(n % (6 * i - 1) == 0 or n % (6 * i + 1) == 0):
      return False

  return True */