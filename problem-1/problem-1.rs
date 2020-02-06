use std::env;

fn main() {
  let args: Vec<String> = env::args().collect();
  let val: i32 = args[0].parse().unwrap();
  println!("Answer: {}",euler_1(val));
}

fn euler_1(x: i32) -> i32 {
  let mut result: i32 = 0;
  let x = x/3;
  let y = x/5;
  let mut i = 1;

  while i < x {
    result += 3*i;
    i += 1;
  }
  i = 1;

  while i < y {
    if 5*i % 3 != 0 {
      result += 5*i;
      i += 1;
    }
  }

  result
}
