#include <iostream>
using namespace std;

int euler_3(int n);

int main() {
  int n;
  cout << "Please enter a number here: ";
  cin >> n;
  cout << "Here is your answer: " << euler_3(n) << "\n";
  return 0;
}

int euler_3(int n) {

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
}
