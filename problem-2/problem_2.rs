use std::io;
use std::time::SystemTime;

fn main() {
  println!("Find the sum of the even-valued Fibonacci terms up to a given number.");
  println!("Please enter the number you want to try below. It must be a positive integer. To match with the Project Euler Problem 2, set it to be 4000000.");
  let mut input = String::new();
  io::stdin()
     .read_line(&mut input)
     .expect("error: unable to read user input");
  let val: i64 = input.trim().parse().expect("invalid input");
  println!("Value: {:?}",val);
  let begin = SystemTime::now();
  let res = euler_2(val);
  match begin.elapsed() {
    Ok(elapsed) => {
      println!("It took {:?}", elapsed)
    }
    Err(e) => {
      println!("Timing error: {:?}",e);
    }
  }
  println!("Result: {:?}",res);
}

fn euler_2(n: i64) -> i64 {
  let mut result: i64 = 0;
  let mut i = 1;

  while fibonacci(i) < n {
    i += 1;
    let f = fibonacci(i);
    if f&1==0 {
      result += f;
    }
  }

  result
}

fn fibonacci(n: i64) -> i64 {
  if n == 1 || n == 2 {
    n
  } else {
    n + fibonacci(n-1)
  }
}
