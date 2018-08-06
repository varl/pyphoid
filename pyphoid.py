#!/usr/bin/python3

import argparse
from lib import feed
from lib import dl

if __name__ == '__main__':
  '''// PYPHOID //'''

  parser = argparse.ArgumentParser()
  parser.add_argument('url', help='URL to the podcast feed (RSS/XML)')
  parser.add_argument('-o', '--output-dir',
      help='output directory where the podcast show will be saved')

  group = parser.add_mutually_exclusive_group()
  group.add_argument('-d', '--download', action='store_true',
      help='download available episodes')
  group.add_argument('-l', '--last-only', action='store_true',
      help='only download the most recent episode')
  group.add_argument('-i', '--interactive', action='store_true',
      help='pick what episodes to download (newest first)')

  args = parser.parse_args()

  if args.output_dir:
    directory = args.output_dir
  else:
    directory = None

  f = feed.url(args.url)

  if args.last_only:
    print("Getting the last episode on URL: {}".format(args.url))
    eps_sorted = sorted(f.eps, key=lambda x: x.publish_date, reverse=True)
    status = dl.download(directory, f.title, [eps_sorted[0]])

  if args.download:
    print("Catching up with podcast on URL: {}".format(args.url))
    status = dl.download(directory, f.title, f.eps)

  if args.interactive:
    print("Using interactive mode to retrieve episodes on URL: {}".format(args.url))
    status = dl.download(directory, f.title, f.eps, args.interactive)

  if  not args.output_dir \
      and not args.interactive \
      and not args.last_only \
      and not args.download:
        print("Attempting to parse feed URL: {}".format(args.url))
        src = feed.xml(args.url)
        eps = sorted(feed.eps(src), key=lambda x: x.publish_date, reverse=False)
        for ep in eps:
          print('{} => {}'.format(ep.publish_date, ep.title))

        status = True


  print('All good in the hood? {}'.format(status))


