import os

import updategists as gh_config
import publish_to_wordpress as wp_config

from file_operations import *
from publish_to_wordpress import *
from updategists import *

langs = ['English','Español','Català','Italiano']

# First of all, what languages will I be working in?
languages = {
  '.c':'C',
  '.cpp':'C++',
  '.cs':'C#',
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
# Start with a .md file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
# MARKDOWN FILE FOUND                                                                                                                                                                                                                                                                                                                                                                                                                                             | MARKDOWN FILE NOT FOUND                                                                                                                                                          |
# Search for any code files                                                                                                                                                                                                                                                                                                                                                                                                                                       | Search for any gists                                                                                                                                                             |
# CODE FILE(S) FOUND                                                                                                                                                                               | NO CODE FILES FOUND                                                                                                                                                                                                                                          | GIST(S) FOUND                                                                                                   | NO GISTS FOUND                                                 |
# Search for Gists                                                                                                                                                                                 | Search for Gists                                                                                                                                                                                                                                             | Search for blog post                                                                                            | Search for blog post                                           |
# GIST(S) FOUND                                                                                                                   | NO GISTS FOUND                                                 | GIST(S) FOUND                                                                                                                   | NO GISTS FOUND                                                                                                             | BLOG POST FOUND                          | BLOG POST NOT FOUND                                                  | BLOG POST FOUND                          | BLOG POST NOT FOUND |
# Would you like to update your gists?                                                                                            | Create gists                                                   | Would you like to delete your gists?                                                                                            | Search for blog post                                                                                                       | Would you like to delete your blog post? | Please create a markdown file then we can turn this into a blog post | Would you like to delete your blog post? | end                 |
# Yes                                                            | No                                                             | Search for blog post                                           | Yes                                                            | No                                                             | BLOG POST FOUND                                    | BLOG POST NOT FOUND                                                   | Yes              | No                    | end                                                                  | Yes              | No                    |
# Update gists                                                   | Search for blog post                                           | BLOG POST FOUND                          | BLOG POST NOT FOUND | Delete gists                                                   | Search for blog post                                           | Would you like to update or delete your blog post? | Would you like to create a blog post, even without any code or gists? | Delete blog post | end                   |                                                                      | Delete blog post | end                   |
# Search for blog post                                           | BLOG POST FOUND                          | BLOG POST NOT FOUND | Would you like to update your blog post? | Create blog post    | Search for blog post                                           | BLOG POST FOUND                          | BLOG POST NOT FOUND | Yes                       | No                     | Yes              | No                                                 | end              |                                                                                              | end              |
# BLOG POST FOUND                          | BLOG POST NOT FOUND | Would you like to update your blog post? | Create blog post    | Yes              | No                    | end                 | BLOG POST FOUND                          | BLOG POST NOT FOUND | Would you like to delete your blog post? | end                 | Update / delete blog post | end                    | Create blog post | end                                                |
# Would you like to update your blog post? | Create blog post    | Yes              | No                    | end                 | Update blog post | end                   |                     | Would you like to delete your blog post? | end                 | Yes              | No                    |                     | end                       |                        | end              |
# Yes              | No                    | end                 | Update blog post | end                   |                                                                                      | Yes              | No                    |                     | Delete blog post | end                   |
# Update blog post | end                   |                     | end              |                                                                                                              | Delete blog post | end                   |
# end              | 
#
# Enter a new Project Euler problem to work with or type 'exit' to exit.

print(zeroth_post_date)

while True:
  print('Please either type a Project Euler problem number below, or \'exit\' to exit.')
  cmd = input('Hi Gavin, which Project Euler problem would you like to work with? ')
  if cmd == 'exit':
    break
  problem_number = int(cmd)
  print('First of all, let\'s see if the Markdown file exists...')
  if(markdown_file_exists(problem_number) and not markdown_file_is_empty(problem_number)):
    # MARKDOWN FILE YES
    print('\x1b[2;32;40m' + 'Yes, the Markdown file exists for problem ' + str(problem_number) + '!' + '\x1b[0m')
    print('Now, let\'s find some code files...')
    if (True):
      # MARKDOWN FILE YES, CODE FILES YES
      print('\x1b[2;32;40m' + 'Yes, code files found for problem ' + str(problem_number) + '!' + '\x1b[0m')
      print('\x1b[2;32;40m' + 'Code files found for <config this bit>C, C++, C#, Java, JavaScript, PHP, Python, Rust and TypeScript</config this bit>' + '.' + '\x1b[0m')
      print('Now to see if we have the Gists...')
      gists = get_all_gists_for_user(gh_config.USERNAME)
      if(gists_exist_for_problem(problem_number)):
        # MARKDOWN FILE YES, CODE FILES YES, GISTS YES
        print('\x1b[2;32;40m' + 'Yes, Gists found for problem ' + str(problem_number) + '!' + '\x1b[0m')
        do_next = str(input('Do you want to update your Gists? Yes/No '))
        if(do_next == 'Yes'):
          # UPDATE GISTS
          print('Updating Gists...')
          print('Gists updated.')
        else:
          # DON'T UPDATE GISTS
          print('Very well then! No Gists updated.')
        print('Okay, let\'s see if there is a blog post...')
        blog_post = get_specific_euler_blog_post(problem_number)
        if(blog_post):
          # MARKDOWN FILE YES, CODE FILES YES, GISTS YES, BLOG POST YES
          print('\x1b[2;32;40m' + 'Yes, blog post found for problem ' + str(problem_number) + '!' + '\x1b[0m')
          do_next = str(input('Do you want to update your blog post? Yes/No '))
          if(do_next == 'yes'):
            # UPDATE BLOG POST
            update_blog_post(problem_number,blog_post['id'])
          else:
            # DON'T UPDATE BLOG POST
            print('Very well then!')
        else:
          # MARKDOWN FILE YES, CODE FILES YES, GISTS YES, BLOG POST NO
          print('\x1b[1;31;40m' + 'No blog post for problem ' + str(problem_number) + '.' + '\x1b[0m')
          create_post = str(input('Would you like me to make one? '))
          if(create_post == 'Yes'):
            # CREATE BLOG POST
            publish(build_post(problem_number))
          else:
            # DON'T CREATE BLOG POST
            print('Very well then! Blog post left alone.')
      else:
        #MARKDOWN FILE YES, CODE FILES YES, GISTS NO
        print('\x1b[1;31;40m' + 'No Gists for problem ' + str(problem_number) + '.' + '\x1b[0m')
        print('Creating gists...')
        print('Gists created')
        print('Now let\'s see if there is a blog post...')
        blog_post = get_specific_euler_blog_post(problem_number)
        if(blog_post):
          # MARKDOWN FILE YES, CODE FILES YES, GISTS NO, BLOG POST YES
          print('\x1b[2;32;40m' + 'Yes, blog post found for problem ' + str(problem_number) + '!' + '\x1b[0m')
          do_next = str(input('Do you want to update your blog post? Yes/No '))
          if(do_next == 'yes'):
            # UPDATE BLOG POST
            update_blog_post(blog_post['id'])
          else:
            # DON'T UPDATE BLOG POST
            print('Very well then!')
        else:
          # MARKDOWN FILE YES, CODE FILES YES, GISTS NO, BLOG POST NO
          print('\x1b[1;31;40m' + 'No blog post for problem ' + str(problem_number) + '.' + '\x1b[0m')
          create_post = str(input('Would you like me to make one? '))
          if(create_post == 'Yes'):
            # CREATE BLOG POST
            publish(build_post(problem_number))
          else:
            # DON'T CREATE BLOG POST
            print('Very well then! Blog post left alone.')
    else:
      #MARKDOWN FILE YES, CODE FILES NO
      print('\x1b[1;31;40m' + 'Hmm...no code files for problem ' + str(problem_number) + ' it seems.' + '\x1b[0m')
  else:
    #MARKDOWN FILE NO
    print('\x1b[1;31;40m' + 'Hmm...no Markdown file for problem ' + str(problem_number) + ' it seems.' + '\x1b[0m')
    pass
print('Thank you for using Gavin\'s bot, goodbye!')
