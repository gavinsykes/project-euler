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

if __name__ == '__main__':
  main()