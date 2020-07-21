#include <iostream>
using namespace std;

int euler_2(int n);
int fibonacci(int n);

int main() {
  int n;
  cout << "Please enter a number here: ";
  cin >> n;
  cout << "Here is your answer: " << euler_2(n) << "\n";
  return 0;
}

int euler_2(int n) {
  int result = 0;
  int i = 1;

  while(fibonacci(i) < n) {
    i++;
    f = fibonacci(i);
    if (!f&1) {
      result += f;
    }
  }

  return result;
}

int fibonacci(int n) {
  if(n == 1 || n == 2) {
    return n;
  }

  int[] fibarray = [1,2];

  return n;
}

# Function to work out the fibonacci numbers. Done as an array because it is much much faster than using a recursive function.
def fibonacci(n):
  if (not isinstance(n,int) or n < 1):
    return undefined # Didn't really need this as I'm controlling the input, but you just never know.

  if (n == 1 or n == 2):
    return n

  fibarray = [1,2]
  for i in range (2,n):
    fibarray.append(fibarray[i-1] + fibarray[i-2])

  return fibarray[n-1]

pyfuncs.fullprint(challenge,euler_2,x)
