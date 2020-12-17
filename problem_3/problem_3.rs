use std::io;
use std::time::SystemTime;

fn main() {
  println!("Find the largest prime factor of a given number.");
  println!("Please enter the number you want to try below. It must be a positive integer. To match with the Project Euler Problem 3, set it to be 600851475143.");
  let mut input = String::new();
  io::stdin()
     .read_line(&mut input)
     .expect("error: unable to read user input");
  let val: u64 = input.trim().parse().expect("invalid input");
  println!("Value: {:?}",val);
  let begin = SystemTime::now();
  let res = euler_3(val);
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

fn euler_3(mut n: u64) -> u64 {
  let mut result: u64 = 0;
  while is_even(n) {
    result = 2;
    n >>= 1;
  }

  for i in (3..(n as f64).sqrt() as u64).step_by(2) {
    while n % i == 0 {
      result = i;
      n = n / i;
    }
  }

  if n > 2 {
    result = n;
  }

  result
}

fn is_even(n: u64) -> bool {
  n&1==0
}
