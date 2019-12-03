const euler_15 = n => nCr(2*n,n);

const nCr = (n,r) => {
  if (r > n || n < 1 || r < 1) {
    return undefined;
  }

  return factorial(n) / (factorial(r) * factorial(n-r));
};

const factorial = num => {
  let result = 1,
      n = +num;
  while (n > 1) {
    n--;
    result *= n;
  }
  return result;
}
