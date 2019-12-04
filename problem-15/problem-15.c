#include <stdio.h>

int nCr(int n,int r);
int factorial(int n);

int main() {
  printf("Here is your answer\n");
  return 0;
}

int nCr(int n,int r) {
  int result = factorial(n) / (factorial(r) - factorial(n-r));
  return result;
}

int factorial(int n) {
  int result = 1;
  while (n > 1) {
    result *= n;
    n--;
  }
  return result;
}
