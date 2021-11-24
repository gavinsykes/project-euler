import json
from problem_1 import euler_1

def main():
  with open('problem_1/problem_1_expected_answers.json','r') as expected_answers_file:
    expected_answers_data = expected_answers_file.read()
    expected_answers = json.loads(expected_answers_data)
    print(expected_answers)
    for expected_answer in expected_answers:
      print(f"Input of {expected_answer['input']} should yield {expected_answer['expected_answer']}")
      print(euler_1(expected_answer['input']) == expected_answer['expected_answer'])
      print(f"Input of {expected_answer['input']} yields {euler_1(expected_answer['input'])}")
    expected_answers_file.close()

if __name__ == '__main__':
  main()