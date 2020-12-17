import updategists_config as gh_config
import publish_to_wordpress_config as wp_config

langs = ['English','Español','Català','Italiano']

# First of all, what languages will I be working in?
languages = {
  '.c':'C',
  '.cpp':'C++',
  '.java':'Java',
  '.js':'JavaScript',
  '.php':'PHP',
  '.py':'Python',
  '.rs':'Rust',
  '.ts':'TypeScript'
}

# Which Project Euler Problem would you like to work with?
# Get post number
# +-------+-------+-----------+---------------------------------------------+
# | Files | Gists | Blog post | Action                                      |
# + ------+-------+-----------+---------------------------------------------+
# | True  | True  | True      | Updates only on Gists and Blog Post         |
# | True  | True  | False     | Make Blog Post - possibly then update Gists |
# | True  | False | True      | Make Gists - possibly then update Blog Post |
# | True  | False | False     | Make Gists then make Blog Post              |
# | False | True  | True      | Remove Gists and Blog Post                  |
# | False | True  | False     | Remove Gists                                |
# | False | False | True      | Remove Blog Post                            |
# | False | False | False     | Do nothing                                  |
# +-------+-------+-----------+---------------------------------------------+
# Check if any files exist
# 
# Enter a new Project Euler problem to work with or type 'exit' to exit.

def pick_language(langs):
  print('Language selection/selección de lengua/selecció de llengua/selezione di lingua:')
  print('THIS ISN\'T WORKING YET, IT WILL ONLY DO ENGLISH')
  for i, el in enumerate(langs):
    print('{}) {}'.format(i+1,el))
  inp = input('Make your choice: ')
  try:
    if 0 < int(inp) <= len(langs):
      return int(inp)
  except:
    pass
  return None

pick_language(langs)

problem_number = int(input('Hi Gavin, which Project Euler problem would you like to work with? '))
