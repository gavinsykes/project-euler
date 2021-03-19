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

def get_all_euler_blog_posts():
  return requests.get(url=config.URL + '?search=Project Euler Problems',headers=config.HEADERS).json()

def get_specific_euler_blog_post(problem_number):
  import html
  result = list(filter(lambda p: html.unescape(p['title']['rendered']) == 'Solving the Project Euler Problems – Problem ' + str(problem_number), get_all_euler_blog_posts()))
  if len(result) == 0:
    return None
  return result[0]

def update_blog_post(problem_number,blog_post_id):
  p = requests.get(url=config.URL + '/' + str(blog_post_id),headers=config.HEADERS).json()
  post = {'content':get_file_contents(problem_number),
          'categories':p['categories'],
          'tags':p['tags']
         }
  change_categories = str(input('Current categories are ' + str(post['categories']) + ', would you like to add or remove any? Yes/no '))
  change_tags = str(input('Current tags are ' + str(post['tags']) + ', would you like to add or remove any? Yes/no '))
  #u = requests.post(url=config.URL + '/' + str(blog_post_id),headers=config.HEADERS,json=post)
  #print(u)
  #print('Tutto bene! Your updated post is at ' + json.loads(u.content)['link'])

def delete_blog_post(blog_post_id):
  d = requests.post(url=config.URL + '/' + str(blog_post_id),headers=config.HEADERS,json=post)
  print(d)

def markdown_file_exists(problem_number):
  return os.path.isfile(workingdirectory + '/problem_' + str(problem_number) + '/problem_' + str(problem_number) + '.md')

def file_is_empty(filename):
  return os.stat(filename).st_size == 0

def markdown_file_is_empty(problem_number):
  return file_is_empty(workingdirectory + '/problem_' + str(problem_number) + '/problem_' + str(problem_number) + '.md')

def get_file_contents(number):
  os.chdir(workingdirectory + '/problem_' + str(number))
  fi = open('problem_' + str(number) + '.md','r')
  if fi.mode == 'r':
    contents = fi.read()
    return json.dumps(contents)

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
  post = {
    'title':'Solving the Project Euler Problems - Problem ' + str(problem_number),
    'date':post_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
    'status':'publish',
    'content':get_file_contents(problem_number),
    'format':'standard'
  }
# 'categories':['Mathematics','Project Euler','Software Development'],
# 'tags':['euler','project euler']
#         }
#  post['categories'].extend(str(input('Would you like to add any additional categories to your post? Perhaps "Mathematics" or "Web Development". ')).split(','))
#  post['tags'].extend(add_tags(problem_number))
#  post['tags'].extend(str(input('Would you also like to add any additional tags to your post? Perhaps "mathematics", "palindrome" or "Fibonacci". ')).split(','))
  print('Okay, here is what your post looks like:')
  print(post)
  return post

def publish(post):
  print(post)
  p = requests.post(url=config.URL,headers=config.HEADERS,json=json.dumps(post))
  print(p)
  print('Tutto bene! Your new post is at ' + json.loads(p.content)['link'])
