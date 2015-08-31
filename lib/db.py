import json

from lib.feed import scan

def push(url, db):
  feed = scan(url)
  return db[:] + feed

def write(db, target):
  print("Active database: {}".format(target))
  print("Dumping database:")
  print(json.dumps(db))
