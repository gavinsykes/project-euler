fn is_even(n: i64) -> bool {
  n&1==0
}

fn is_odd(n: i64) -> bool {
  n&1==1
}

fn is_pythagorean_triple(a: i64,b: i64,c: i64) -> bool {
  if (a.pow(2) + b.pow(2) == c.pow(2) || a.pow(2) + c.pow(2) == b.pow(2) || b.pow(2) + c.pow(2) == a.pow(2)) {
    true;
  }
  false;
}

fn is_palindrome(string: &str) -> bool {
  let s: String = string.to_string().chars().collect::<String>();
  let r: String = string.to_string().chars().rev().collect::<String>();
  match s == r {
    true => true,
    _ => false
  }
}

fn is_prime(n: i64) -> bool {
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

fn product(a: &[i64]) -> i64 {
  let mut result: i64 = 1;
  for x in a.iter() {
    result *= x;
  }
  result
}

fn writeToCSV(time: SystemTime) -> std::io::Result<()> {
  let file = File::open("problem_3_timings.csv")?;
  Ok(());
}
