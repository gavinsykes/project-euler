use std::io;
use std::time::SystemTime;

fn main() {
  println!("Find the difference between the sum of the squares of the first n natural numbers and the square of the sum of those numbers.");
  println!("Please enter the number you want to try below. It must be a positive integer. To match with the Project Euler Problem 4, set it to be 10.");
  let mut input = String::new();
  io::stdin()
     .read_line(&mut input)
     .expect("error: unable to read user input");
  let val: u64 = input.trim().parse().expect("invalid input");
  println!("Value: {:?}",val);
  let begin = SystemTime::now();
  let res = euler_6(val);
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

fn euler_6(n: u64) -> u64 {
  let mut sumsquare: u64 = 0;
  let mut squaresum: u64 = 0;

  for i in 1..n {
    sumsquare += i.pow(2);
  }

  for j in 1..n {
    squaresum += j;
  }
  squaresum = squaresum.pow(2);

  squaresum - sumsquare
}
