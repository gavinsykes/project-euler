from typing import Callable
from numpy import min,max,mean,std
from tabulate import tabulate
from time import perf_counter

def even_modulo(n: int) -> bool:
  return n % 2 == 0

def even_binary(n: int) -> bool:
  return not(n & 1)

def even_check_last_digit(n: int) -> bool:
  return str(n)[-1] in (2,4,6,8,0)

def time_function(name: str, fun: Callable, arg: int) -> float:
  start = perf_counter()
  fun(arg)
  end = perf_counter()
  print(f"{name}:\t\t\t{end-start}")
  return end-start

def compare_even_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['binary_list'].append(time_function("Binary",even_binary,i))
    result_lists['check_last_digit_list'].append(time_function("Check last digit",even_check_last_digit,i))
    result_lists['modulo_list'].append(time_function("Modulo",even_modulo,i))

def divisible_by_3_digit_sum(n: int) -> bool:
  num_as_string = str(n)
  sum_digits = sum(map(int, num_as_string))
  if sum_digits > 9:
    return divisible_by_3_digit_sum(sum_digits)
  if sum_digits in (3,6,9):
    return True
  return False

def divisible_by_3_modulo(n: int) -> bool:
  return n % 3 == 0

def compare_divisible_by_3_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['check_digit_sum_list'].append(time_function("Check Digit Sum",divisible_by_3_digit_sum,i))
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_3_modulo,i))

def divisible_by_4_modulo(n: int) -> bool:
  return n % 4 == 0

def divisible_by_4_binary(n: int) -> bool:
  return not(n & 3)

def compare_divisible_by_4_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['binary_list'].append(time_function("Binary",divisible_by_4_binary,i))
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_4_modulo,i))

def divisible_by_5_modulo(n: int) -> bool:
  return n % 5 == 0

def divisible_by_5_check_digit(n: int) -> bool:
  return int(str(n)[-1]) in (0,5)

def compare_divisible_by_5_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['check_last_digit_list'].append(time_function("Binary",divisible_by_5_check_digit,i))
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_5_modulo,i))

def divisible_by_6_modulo(n: int) -> bool:
  return n % 6 == 0

def divisible_by_6_composite(n: int) -> bool:
  return even_modulo(n) and divisible_by_3_modulo(n)

def compare_divisible_by_6_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_6_modulo,i))
    result_lists['composite_list'].append(time_function("Composite (2 modulo and 3 modulo)",divisible_by_6_composite,i))

def divisible_by_7_modulo(n: int) -> bool:
  return n % 7 == 0

def divisible_by_7_algorithm(n: int) -> bool:
  if n < 7:
    return False
  if n in (7,14,21,28,35,42,49,56,63,70,77,84,91,98,105,112,119,126,133,140):
    return True
  last_digit_doubled = int(str(n)[-1]) * 2
  remainder = int(str(n)[-1:])
  result = remainder - last_digit_doubled
  if result not in range(7,141):
    return divisible_by_7_algorithm(result)
  if result in (0,7,14,21,28,35,42,49,56,63,70,77,84,91,98,105,112,119,126,133,140):
    return True
  return False

def compare_divisible_by_7_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_7_modulo,i))
    result_lists['algorithm_list'].append(time_function("Algorithm",divisible_by_7_algorithm,i))

def divisible_by_8_modulo(n: int) -> bool:
  return n % 8 == 0

def divisible_by_8_binary(n: int) -> bool:
  return not n & 7

def compare_divisible_by_8_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['binary_list'].append(time_function("Binary",divisible_by_8_binary,i))
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_8_modulo,i))
def compare_divisible_by_9_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_9_modulo,i))
def compare_divisible_by_10_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_10_modulo,i))
def compare_divisible_by_11_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_11_modulo,i))
def compare_divisible_by_12_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_12_modulo,i))
def compare_divisible_by_13_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_13_modulo,i))
def compare_divisible_by_14_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_14_modulo,i))
def compare_divisible_by_15_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_15_modulo,i))
def compare_divisible_by_16_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_16_modulo,i))
def compare_divisible_by_17_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_17_modulo,i))
def compare_divisible_by_18_functions() -> None:
  for i in loop_range:
    print(f"{i}:")
    result_lists['modulo_list'].append(time_function("Modulo",divisible_by_18_modulo,i))

result_lists = {
  'algorithm_list': [],
  'binary_list': [],
  'check_last_digit_list': [],
  'check_digit_sum_list': [],
  'composite_list': [],
  'modulo_list': []
}
data = []
number_of_runs = 100
loop_range = range(1,number_of_runs + 1)

def main():
  base = 8
  compare_divisible_by_8_functions()
  for name,list in result_lists.items():
    if list:
      data.append([name,min(list),max(list),mean(list),std(list),sum(list)])
  print(f"\x1b[1mDividing by {base}\x1b[0m")
  print(tabulate(data,headers = ["Function","Min","Max","Mean","Std Dev","Total"]))

if __name__ == '__main__':
  main()