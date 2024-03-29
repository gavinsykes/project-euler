pub fn is_even(n: i64) -> bool {
  n&1==0
}

pub fn is_odd(n: i64) -> bool {
  n&1==1
}

pub fn is_pythagorean_triple(a: u64,b: u64,c: u64) -> bool {
  let a_squared: u64 = a.pow(2);
  let b_squared: u64 = b.pow(2);
  let c_squared: u64 = c.pow(2);
  if (a_squared + b_squared == c_squared || a_squared + c_squared == b_squared || b_squared + c_squared == a_squared) {
    true;
  }
  false;
}

pub fn is_palindrome(string: &str) -> bool {
  let s: String = string.to_string().chars().collect::<String>();
  let r: String = string.to_string().chars().rev().collect::<String>();
  match s == r {
    true => true,
    _ => false
  }
}

pub fn is_prime(n: u64) -> bool {
  if n < 1 || is_even(n) {
    return false;
  }

  if n == 3 || n == 5 {
    return true;
  }

  if n % 3 == 0 {
    return false;
  }

  if n.to_string().chars().last().unwrap() == '5' || n.to_string().chars().last().unwrap() == '0' {
    return false;
  }

  for i in 1..n/6 {
    if n % (6 * i - 1) == 0 || n % (6 * i + 1) == 0 {
      return false;
    }
  }

  true
}

pub fn product(a: &[i64]) -> i64 {
  let mut result: i64 = 1;
  for x in a.iter() {
    result *= x;
  }
  result
}

pub fn writeToCSV(time: SystemTime) -> std::io::Result<()> {
  let file = File::open("problem_3_timings.csv")?;
  Ok(());
}
