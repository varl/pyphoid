import json
import sqlite3

conn = sqlite3.connect('../database.db')

def add(feed):
  c = conn.cursor()
  try:
    c.execute('INSERT INTO feeds VALUES (?, ?, ?, ?)', \
        feed.title, feed.url, feed.last_updated, feed.files)
  except sqlite3.OperationalError as e:
    print("Error occured {}".format(e.args[0]))
    return False, e
    
  return True, feed

def write(db, target):
  print("Active database: {}".format(target))
  print("Dumping database:")
  print(json.dumps(db))
