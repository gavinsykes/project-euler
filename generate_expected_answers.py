from json import loads, dumps
from os import path
from sys import path as syspath

def main():
  problem_number = int(input("Which problem number do you want to generate the answers for? "))

  """
  Import the euler_x function from the problem_x script
  """
  syspath.append(path.dirname(__file__) + f'/problem_{problem_number}')
  try:
    _import = __import__(f'problem_{problem_number}', globals(), locals(), [f'euler_{problem_number}'], 0)
    euler_function = _import.__dict__[f'euler_{problem_number}']
  except ModuleNotFoundError:
    print(f"\x1b[1;31mIt doesn't look like a Python script has been written yet for problem {problem_number}, exiting...\x1b[0m")
    return
  try:
    with open(path.dirname(__file__) + f'problem_{problem_number}/problem_{problem_number}_expected_answers.json','r') as expected_answers_file:
      current_expected_answers_data = expected_answers_file.read()
      current_expected_answers = loads(current_expected_answers_data)
  except FileNotFoundError:
    current_expected_answers = []
  finally:
    print("You will now be asked for the range of inputs for which you wish to generate the answers, starting with, rather creatively, the starting point, then the end point, then the step size (usually 1 but you'll want to make it bigger for really big ranges going into the millions).")
    starting_point = int(input("Where would you like to start? (Usually 1) "))
    end_point = int(input("Where would you like to end? "))
    step_size = int(input("What should the step size be? (Usually 1 or a power of 10) "))
    for i in range(starting_point,end_point+1,step_size):
      current_expected_answers.append({'input':i,'expected_answer':euler_function(i)})
    with open(path.dirname(__file__) + f'/problem_{problem_number}/problem_{problem_number}_expected_answers.json','w') as updated_answers_file:
      updated_answers_file.write(dumps(current_expected_answers))

if __name__ == '__main__':
  main()