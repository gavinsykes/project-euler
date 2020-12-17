import publish_to_wordpress_config as config

import requests
import json
import os
from datetime import datetime, timedelta

zeroth_post_date = datetime(2018,12,30,15,0,0)
workingdirectory = os.getcwd()

language_extensions = {'.c':'C',
                       '.cpp':'C++',
                       '.java':'Java',
                       '.js':'JavaScript',
                       '.php':'PHP',
                       '.py':'Python',
                       '.rs':'Rust',
                       '.ts':'TypeScript'
                      }

def get_file_contents(number):
  os.chdir(workingdirectory + '/problem_' + str(number))
  fi = open('problem_' + str(number) + '.md','r')
  if fi.mode == 'r':
    contents = fi.read()
    return contents

def add_tags(problem_number):
  result = list()
  os.chdir(workingdirectory + '/problem_' + str(problem_number))
  for key, value in language_extensions.items():
    if os.path.isfile('problem_' + str(problem_number) + key):
      if not os.stat('problem_' + str(problem_number) + key).st_size == 0:
        result.append(value)
  return result

def build_post(problem_number):
  if ( (problem_number < 1) or (not isinstance(problem_number, int)) ):
    raise Exception(f'You entered {problem_number}, which is either not an integer or not greater than or equal to 1!')
  post_date = zeroth_post_date + timedelta(days = problem_number * 7)
  post = {'title':'Solving the Project Euler Problems - Problem ' + str(problem_number),
          'date':post_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
          'status':'publish',
          'content':get_file_contents(problem_number),
          'comment_status':'open',
          'format':'standard',
          'categories':['Mathematics','Project Euler','Software Development'],
          'tags':['euler','project euler']
         }
  post['categories'].extend(str(input('Would you like to add any additional categories to your post? Perhaps "Mathematics" or "Web Development". ')).split(','))
  post['tags'].extend(add_tags(problem_number)).extend(str(input('Would you also like to add any additional tags to your post? Perhaps "mathematics", "palindrome" or "Fibonacci". ')).split(','))
  print(post)

def publish(post):
  p = requests.post(url=config.URL,headers=config.HEADERS,json=post)
  print(p)
  print('Tutto bene! Your new post is at ' + json.loads(p.content)['link'])

post_to_submit = build_post(int(input('Hi Gavin, which Project Euler Problem do you want to build a blog post for? ')))

publish(post_to_submit)
