use std::io;
use std::time::SystemTime;

fn main() {
  println!("Find the largest palindrome from the product of 2 numbers of a given length.");
  println!("Please enter the number you want to try below. It must be a positive integer. To match with the Project Euler Problem 4, set it to be 3.");
  let mut input = String::new();
  io::stdin()
     .read_line(&mut input)
     .expect("error: unable to read user input");
  let val: u32 = input.trim().parse().expect("invalid input");
  println!("Value: {:?}",val);
  let begin = SystemTime::now();
  let res = euler_4(val);
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

fn euler_4(n: u32) -> u64 {
  let mut result: u64 = 0;
  for i in 1..10_u64.pow(n) {
    for j in 1..10_u64.pow(n) {
      if is_palindrome((i*j).to_string()) && i*j > result {
        result = i*j;
      }
    }
  }
  result
}

fn is_palindrome(string: String) -> bool {
  let s: String = string.to_string().chars().collect::<String>();
  let r: String = string.to_string().chars().rev().collect::<String>();
  match s == r {
    true => true,
    _ => false
  }
}
