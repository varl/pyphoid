#!/usr/bin/python3

import sys
import os
import argparse
from lib import db, feed
from urllib import request


"""
Download the feed
"""
def download(title, eps):
  total = len(eps)

  if not os.path.exists(title):
    os.makedirs(title)

  for index, ep in enumerate(eps):
    print('{}, {}'.format(ep.title, title))
    ep_name = os.path.join(title, ep.title+'.mp3')

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

  parser.add_argument("-d", "--download")
  parser.add_argument("-l", "--last-one")

  args = parser.parse_args()

  if args.last_one:
    print("Getting the last episode on URL: {}".format(args.last_one))
    f = feed.url(args.last_one)
    
    # sort by publish date and get the last (=newest) item
    last_ep = sorted(f.eps, key=lambda x: x.publish_date)[-1]

    status = download(f.title, [last_ep])

  if args.download:
    print("Catching up with podcast on URL: {}".format(args.add_url))
    f = feed.url(args.add_url)

    print('Downloading episodes...')
    status = download(f.title, f.eps)

  print('All good in the hood? {}'.format(status))
