#!/usr/bin/python3

import sys
import os
import argparse
from lib import feed
from urllib import request


"""
Download the feed
"""
def download(title, eps):
  total = len(eps)

  if not os.path.exists(title):
    os.makedirs(title)

  for index, ep in enumerate(eps):
    ep_name = os.path.join(title, ep.publish_date+'_'+ep.title+'.mp3')

    if not os.path.exists(ep_name):
      print('({}/{}) => {}'.format(index, total, ep_name))
      request.urlretrieve(ep.url, ep_name)
    else:
      print('ERR: "{}" already exists'.format(ep_name))
      continue

  return True

"""
Main logic
"""
if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument('url', help='URL to the podcast feed (RSS/XML)')
  parser.add_argument('-d', '--download', action='store_true')
  parser.add_argument('-l', '--last-only', action='store_true')

  args = parser.parse_args()

  f = feed.url(args.url)

  if args.last_only:
    print("Getting the last episode on URL: {}".format(args.url))
    eps_sorted = sorted(f.eps, key=lambda x: x.publish_date, reverse=True)
    status = download(f.title, [eps_sorted[-1]])

  if args.download:
    print("Catching up with podcast on URL: {}".format(args.url))
    status = download(f.title, f.eps)

  print('All good in the hood? {}'.format(status))
