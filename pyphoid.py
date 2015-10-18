#!/usr/bin/python3

import sys
import argparse
from lib import db, feed

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--add-url")
parser.add_argument("--catch-up", action="store_true")
parser.add_argument("--last-one", action="store_true")

args = parser.parse_args()

if args.catch_up:
  print("Calling function to catch-up")

if args.last_one:
  print("Calling function to get last one")

if args.add_url:
  print("Got URL: {}".format(args.add_url))
  f = feed.scan(args.add_url)
  status, result = db.add(f)
  print("Status was {}, result: {}".format(status, result))



