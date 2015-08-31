import xml.etree.ElementTree as ET
import urllib.request as req

from collections import namedtuple
from datetime import datetime

Feed = namedtuple('Feed', \
  ['url', 'title', 'files', 'last_update'])

def scan(url):
  feed = make_feed(url)
  return Feed(url=url, \
      title=title(feed), \
      files=eps(feed), \
      last_update=datetime.utcnow().isoformat())

def make_feed(url):
  with req.urlopen(url) as resp:
    return ET.fromstring(resp.read())

def title(feed):
  return feed.find('channel').find('title').text

def eps(feed):
  return list(map(lambda x: x.find('title').text.strip('\n'), feed.find('channel').findall('item')))
