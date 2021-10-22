const fs = require('fs');

const isEven = n => !n&1;
const isOdd = n => n&1;

const isPalindrome = n => n.toString().split('').every((c,i) => c === n.toString().split('').reverse()[i]);

const productOfArray = array => array.reduce((accumulator,current) => current * accumulator,1);

const isPythagoreanTriple = (a,b,c) => {
  const a_squared = a**2;
  const b_squared = b**2;
  const c_squared = c**2;
  return a_squared + b_squared == c_squared || a_squared + c_squared == b_squared || b_squared + c_squared == a_squared
};

const isPrime = n => {
  if (
    !Number.isInteger(n) || // The number must be an integer to be prime
    n < 1 || // It must also be 1 or more, there's a huge debate about whether 1 is prime or not, I say it is.
    (isEven(n) && n != 2) || // We can eliminate (almost) half the possible numbers very easily, but remember that 2 itself is prime!
    n % 3 == 0 || // Checking for divisibility by 3 is computationally cheap enough
    n.toString().split().reverse()[0] == "5" || // Check if it ends with a 5
    n.toString().split().reverse()[0] == "0" // Or a 0
  ) {
    return false
  }

  // Now the fun bit!
  for (let i = 1; i < n/6; i++) {
    if (n % (6 * i - 1) == 0 || n % (6 * i + 1) == 0) {
      return false;
    }
  }
  return true;
}

const fullPrint = (challenge,fun,argument) => {
  const problem_number = new Error().stack.split("\n")[2].split('.js')[0].split("_").reverse()[0];
  const timing = {};
  timing.start = Date.now();
  result = argument ? fun(argument) : fun();
  timing.finish = Date.now();
  console.log(challenge);
  console.log(`Start time: ${timing.start}`);
  console.log(`Result: ${result}`);
  console.log(`Finish time: ${timing.finish}`);
  console.log(`This returns ${result} in ${timing.finish - timing.start} seconds!`);
  node_v = process.versions.v8.split('.');
  const { exec } = require('child_process');
  exec(`python3 ./file_operations.py --csv -l=JavaScript -g=${node_v[0]}.${node_v[1]}.${node_v[2]} -n=${problem_number} -i=${argument} -t=${timing.finish - timing.start} -s=${timing.start}`);
}
  
  module.exports = {
    fullPrint: fullPrint,
    isEven: isEven,
    isOdd: isOdd,
    isPalindrome: isPalindrome,
    isPrime: isPrime,
    isPythagoreanTriple: isPythagoreanTriple,
    productOfArray: productOfArray
  };