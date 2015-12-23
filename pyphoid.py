#!/usr/bin/python3

import sys
import os
import argparse
from lib import feed
from urllib import request

def download(title, eps, interactive=False):
  '''Downloads episodes based on the podcast name in the directory:
  `<title>/<date>_<episode title>.mp3`
  
  TODO: Implement custom name format
  TODO: Support true file type instead of hardcoding mp3
  '''

  total = len(eps)

  if not os.path.exists(title):
    os.makedirs(title)

  for index, ep in enumerate(eps):
    ep_name = os.path.join(title, ep.publish_date+'_'+ep.title+'.mp3')

    if not os.path.exists(ep_name):
      if interactive:
        print('')
        print('Title:\t\t{}'.format(ep.title))
        print('--------')
        print('Published:\t{}'.format(ep.publish_date))
        print('URL:\t\t{}'.format(ep.url))
        print('Description:\t{}'.format(ep.description))
        print('--------')

        confirmation = respond('Download (y/n)? ')
        if confirmation:
          print('({}/{}) => {}'.format(index, total, ep_name))
          request.urlretrieve(ep.url, ep_name)
        else:
          continue

      else:
        print('({}/{}) => {}'.format(index, total, ep_name))
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

  return response




if __name__ == '__main__':
  '''// PYPHOID //'''

  parser = argparse.ArgumentParser()
  parser.add_argument('url', help='URL to the podcast feed (RSS/XML)')

  group = parser.add_mutually_exclusive_group()
  group.add_argument('-d', '--download', action='store_true',
      help='download available episodes')
  group.add_argument('-l', '--last-only', action='store_true',
      help='only download the most recent episode')
  group.add_argument('-i', '--interactive', action='store_true',
      help='pick what episodes to download (newest first)')

  args = parser.parse_args()

  f = feed.url(args.url)

  if args.last_only:
    print("Getting the last episode on URL: {}".format(args.url))
    eps_sorted = sorted(f.eps, key=lambda x: x.publish_date, reverse=True)
    status = download(f.title, [eps_sorted[-1]])

  if args.download:
    print("Catching up with podcast on URL: {}".format(args.url))
    status = download(f.title, f.eps)

  if args.interactive:
    print("Using interactive mode to retrieve episodes on URL: {}".format(args.url))
    status = download(f.title, f.eps, args.interactive)

  print('All good in the hood? {}'.format(status))


