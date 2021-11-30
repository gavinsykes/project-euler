from json import loads
from os import path

problem_number = path.basename(__file__).split('.')[0].split('_')[-2]
_import = __import__(f'problem_{problem_number}', globals(), locals(), [f'euler_{problem_number}'], 0)
euler_function = _import.__dict__[f'euler_{problem_number}']

def main():
  with open(path.dirname(__file__) + f'/problem_{problem_number}_expected_answers.json','r') as expected_answers_file:
    expected_answers_data = expected_answers_file.read()
    expected_answers = loads(expected_answers_data)
    expected_answers_file.close()

  successful_tests = 0
  failed_tests = []
  for expected_answer in expected_answers:
    print(f"Input of {expected_answer['input']} should yield {expected_answer['expected_answer']}")
    success = False
    format_character = '\033[1;31m'
    answer = euler_function(expected_answer['input'])
    if answer == expected_answer['expected_answer']:
      successful_tests += 1
      success = True
    else:
      failed_tests.append({'input':expected_answer['input'],'expected_answer':expected_answer['expected_answer'],'actual_answer':answer})
    if success:
      format_character = '\033[1;32m'
    closing_format_character = '\033[0m'
    print(f"{format_character}Input of {expected_answer['input']} yields {answer}{closing_format_character}")

  total_tests = successful_tests + len(failed_tests)
  print(f"\033[1mTotal tests: {total_tests}\033[0m")
  print(f"\033[1;32mSuccessful tests: {successful_tests} ({successful_tests * 100 / total_tests}%)\033[0m")
  if len(failed_tests) > 0:
    print(f"\033[1;31mFailed tests: {len(failed_tests)} ({len(failed_tests) * 100 / total_tests}%)\033[0m")
    for test in failed_tests:
      print(f"\033[1;31mInput of {test['input']} should have yielded {test['expected_answer']} but yields {test['actual_answer']}\033[0m")

if __name__ == '__main__':
  main()