import xml.etree.ElementTree as ET
import urllib.request as req

from collections import namedtuple
from datetime import datetime


"""
Feed and Ep structures
"""

Feed = namedtuple('Feed', \
  ['title', 'eps'])
                    
Ep = namedtuple('Ep', \
    ['title', 'url', 'description', 'publish_date'])

"""
Interface
"""
def url(url):
  return make(xml(url))


"""
Internal
"""
def make(src):
  return Feed(title=title(src), \
      eps=eps(src))

def xml(url):
  with req.urlopen(url) as resp:
    return ET.fromstring(resp.read())

def title(src):
  return find('channel', src).find('title').text

def eps(src):
  return list(map(extract_ep, \
      find('channel', src).findall('item')))


"""
Helpers
"""
def extract_ep(src):
  title = find_text('title', src)

  description = find_text('media:description', src)
  if description is None:
    description = find_text('description', src)

  url = find_url('media:content', src)
  if url is None:
    url = find_url('enclosure', src)

  publish_date = find_text('pubDate', src)
  pubdate = convert(publish_date)

  return Ep(title=title, \
            url=url, \
            description=description, \
            publish_date=pubdate.isoformat())

def convert(date):
  return datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %z')

def find(attr, element):
  namespace = {
    'media': 'http://search.yahoo.com/mrss/'
  }

  try:
    if len(attr.split(':')) > 1:
      return element.find(attr, namespace)
    else:
      return element.find(attr)

  except AttributeError:
    return None

def find_text(attr, element):
  return find(attr, element).text.strip('\n')

def find_url(attr, element):
  return find(attr, element).get('url', None)

