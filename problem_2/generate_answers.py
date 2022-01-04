from json import loads, dumps
from os import path

# Extract the problem number from the filepath
problem_number = path.dirname(__file__).split('_')[-1]

"""
Import the euler_x function from the problem_x script, this is to save
rewriting the number every time I move it to a different subfolder
"""
_import = __import__(f'problem_{problem_number}', globals(), locals(), [f'euler_{problem_number}'], 0)
euler_function = _import.__dict__[f'euler_{problem_number}']

def main():
  with open(path.dirname(__file__) + f'/problem_{problem_number}_expected_answers.json','r') as expected_answers_file:
    current_expected_answers_data = expected_answers_file.read()
    current_expected_answers = loads(current_expected_answers_data)
  for i in range(4_000_001,5_000_001):
    current_expected_answers.append({'input':i,'expected_answer':euler_function(i)})
  with open(path.dirname(__file__) + f'/problem_{problem_number}_expected_answers.json','w') as updated_answers_file:
    updated_answers_file.write(dumps(current_expected_answers))

if __name__ == '__main__':
  main()