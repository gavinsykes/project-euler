from json import loads, dumps
from os import path
from problem_1 import euler_1 as euler_function

def main():
  with open(path.dirname(__file__) + '/problem_1_expected_answers.json','r') as expected_answers_file:
    current_expected_answers_data = expected_answers_file.read()
    current_expected_answers = loads(current_expected_answers_data)
    expected_answers_file.close()
  for i in range(41,1001):
    current_expected_answers.append({'input':i,'expected_answer':euler_function(i)})
  with open(path.dirname(__file__) + '/problem_1_expected_answers.json','w') as updated_answers_file:
    updated_answers_file.write(dumps(current_expected_answers))
    updated_answers_file.close()
"""
  for expected_answer in expected_answers:
    print(f"Input of {expected_answer['input']} should yield {expected_answer['expected_answer']}")
    success = False
    format_character = '\033[1;31m'
    answer = euler_function(expected_answer['input'])
    if answer == expected_answer['expected_answer']:
      success = True
    if success:
      format_character = '\033[1;32m'
    closing_format_character = '\033[0m'
    print(f"{format_character}Input of {expected_answer['input']} yields {answer}{closing_format_character}")
"""
if __name__ == '__main__':
  main()