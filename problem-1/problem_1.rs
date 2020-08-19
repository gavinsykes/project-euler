use std::io;
use std::time::SystemTime;

fn main() {
  println!("Find the sum of all the multiples of 3 or 5 below a given number.");
  println!("Please enter the number you want to try below. It must be a positive integer. To match with the Project Euler Problem 1, set it to be 1000.");
  let mut input = String::new();
  io::stdin()
     .read_line(&mut input)
     .expect("error: unable to read user input");
  let val: i64 = input.trim().parse().expect("invalid input");
  println!("Value: {:?}",val);
  let begin = SystemTime::now();
  let res = euler_1(val);
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

fn euler_1(n: i64) -> i64 {
  let mut result: i64 = 0;
  let x: i64 = (n as f64/3.0).ceil() as i64;
  let y: i64 = (n as f64/5.0).ceil() as i64;
  let mut i = 1;

  while i < x {
    result += 3*i;
    i +=1;
  }

  i = 1;

  while i < y {
    if 5*i %3 !=0 {
      result += 5*i;
    }
    i +=1;
  }

  result
}
