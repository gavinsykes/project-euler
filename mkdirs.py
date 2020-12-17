import os

working_directory = os.getcwd()
extensions = ['.c','.cpp','.java','.js','.md','.php','.py','.rs','.ts']

def mkdirs():
  for i in range(1,736):
    path = working_directory + '/problem_' + str(i)
    if not os.path.isdir(path):
      try:
        os.mkdir(path)
      except:
        print(f'Creation of the directory {path} failed')
      else:
        print(f'Creation of the directory {path} was great success!')
    else:
      print(f'Directory {path} already exist')

def mkfiles():
  for i in range(1,736):
    os.chdir(working_directory + '/problem_' + str(i))
    if not os.path.isfile('problem_' + str(i) + '_timings.csv'):
      try:
        file = open('problem_' + str(i) + '_timings.csv','w')
        file.close()
      except:
        print(f'Creation of the timings CSV in problem_{i} failed')
      else:
        print(f'Creation of the timings CSV in problem_{i} was great success!')
    for ext in extensions:
      if not os.path.isfile('problem_' + str(i) + ext):
        try:
          file = open('problem_' + str(i) + ext,'w')
          file.close()
        except:
          print(f'Creation of {ext} file in problem_{i} failed')
        else:
          print(f'Creation of {ext} file in problem_{i} was great success!')
      else:
        print(f'Problem {i} {ext} file already exist')

mkfiles()
