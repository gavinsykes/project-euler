#include <stdio.h>

int main() {
  printf("Here is your answer\n");
  return 0;
}

int is_prime(n) {
  if(!n&1):
    return 0;
  if(n%3==0):
    return 0;
  if(num%10==5 || num%10==0):
    return 0;
  int i;
  for (i=1;i<n/6;i++) {
    if(n % (6 * i - 1) == 0 or n % (6 * i + 1) == 0) {
      return 0;
    }
  }

  return 1;
}
