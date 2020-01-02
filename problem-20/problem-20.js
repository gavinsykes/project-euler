const factorial = n => {
  let res = n;
  if (!Number.isInteger(n) || n < 0) {
    return undefined;
  }
  if (n === 0 || n === 1) 
    return 1; 
  while (n > 1) { 
    n--;
    result *= n;
  }
  return result;
};

const euler_20 = n => {
  return factorial(n).toString().split('').reduce((acc,c) => acc += +c,0);
};
