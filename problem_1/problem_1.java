import java.util.Scanner;

class problem_1 {
  static int euler_1(int n) {
    int result = 0;
    double x = n/3;
    double y = n/5;

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
  public static void main(String[] args) {
    System.out.println("Please enter a number here: ");
    Scanner s = new Scanner(System.in);
    int n = s.nextInt();
    System.out.println(euler_1(n));
  }
}
