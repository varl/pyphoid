import xml.etree.ElementTree as ET
import urllib.request as req

from collections import namedtuple
from datetime import datetime

namespace = {'media': 'http://search.yahoo.com/mrss/'}

Feed = namedtuple('Feed', \
  ['url', 'title', 'eps', 'last_update'])
                    
Ep = namedtuple('Ep', \
    ['title', 'url', 'description', 'thumbnail', 'publish_date'])

def scan(url):
  feed = make_feed(url)
  return Feed(url=url, \
      title=title(feed), \
      eps=eps(feed), \
      last_update=datetime.utcnow().isoformat())

def make_feed(url):
  with req.urlopen(url) as resp:
    return ET.fromstring(resp.read())

def title(feed):
  return feed.find('channel').find('title').text

def eps(feed):
  return list(map(extract_ep, \
      feed.find('channel').findall('item')))

def extract_ep(el):
  try:
    title = el.find('title').text.strip('\n')
  except AttributeError:
    title = None

  try:
    url = el.find('media:content', namespace).get('url', None)
  except AttributeError:
    url = None

  try:
    thumbnail = el.find('media:thumbnail', namespace).get('url', None) 
  except AttributeError:
    thumbnail = None

  try:
    description = el.find('media:description', namespace).text.strip('\n')
  except AttributeError:
    description = el.find('description').text.strip('\n')
  else:
    description = None

  try:
    publish_date = el.find('pubDate').text.strip('\n')
  except AttributeError:
    publish_date = None

  pubdate = convert(publish_date)

  return Ep(title=title, \
            url=url, \
            description=description, \
            thumbnail=thumbnail,
            publish_date=pubdate.isoformat())

def convert(date):
  return datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %z')
