from json import loads, dumps
from os import path

problem_number = path.basename(__file__).split('.')[0].split('_')[-2]
_import = __import__(f'problem_{problem_number}', globals(), locals(), [f'euler_{problem_number}'], 0)
euler_function = _import.__dict__[f'euler_{problem_number}']

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