#include <iostream>
using namespace std;

int euler_1(int n);

int main() {
  int n;
  cout << "Please enter a number here: ";
  cin >> n;
  cout << "Here is your answer: " << euler_1(n) << "\n";
  return 0;
}

int euler_1(int n) {
  int result = 0;
  float x = n/3;
  float y = n/5;

  for(int i = 1; i <= x; i++) {
    result += 3*i;
  }

  for (int i = 1; i <= y; i++) {
    if (5*i % 3 != 0) {
      result += 5*i;
    }
  }

  return result;
}
