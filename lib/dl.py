#!/usr/bin/python3

import os
from urllib import request

def download(directory, title, eps, interactive=False):
  '''Downloads episodes based on the podcast name in the directory:
  `<title>/<date>_<episode title>.mp3`
  
  TODO: Implement custom name format
  TODO: Support true file type instead of hardcoding mp3
  '''
  total = len(eps)

  if directory is None:
    directory = os.getcwd()

  cwd = os.path.join(directory, title)

  if not os.path.exists(cwd):
    os.makedirs(cwd)

  for index, ep in enumerate(eps):
    ep_name = os.path.join(cwd, ep.publish_date+'_'+ep.title+'.mp3')

    if not os.path.exists(ep_name):
      print('({}/{}) => {}'.format(index, total, ep_name))

      if interactive:
        print('')
        print('Title:\t\t{}'.format(ep.title))
        print('Published:\t{}'.format(ep.publish_date))
        print('Description:\t{}'.format(ep.description))
        print('URL:\t\t{}'.format(ep.url))
        print('File:\t\t{}'.format(ep_name))
        print('--------')

        confirmation = respond('Download (y/n)? ')
        if confirmation:
          request.urlretrieve(ep.url, ep_name)
        else:
          continue

      else:
        request.urlretrieve(ep.url, ep_name)

    else:
      print('ERR: "{}" already exists'.format(ep_name))
      continue

  return True


def respond(message):
  '''Make the user answer a y/n question'''

  valid = False
  response = False

  while not valid:
    r = input(message)
    if r.lower() == 'y':
      valid = True
      response = True
    elif r.lower() == 'n':
      valid = True
      response = False
    else:
      pass

  return response


