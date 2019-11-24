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
  if((str(n)[-1:] == '5') || (str(n)[-1:] == '0')):
    return 0;
  for i in range(1,int(math.floor(n/6)),1):
    if(n % (6 * i - 1) == 0 or n % (6 * i + 1) == 0):
      return 0;

  return 1;
}
