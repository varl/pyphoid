import xml.etree.ElementTree as ET
import urllib.request as req

from collections import namedtuple
from datetime import datetime


# struct for feeds and eps
Feed = namedtuple('Feed', \
  ['title', 'eps'])
                    
Ep = namedtuple('Ep', \
    ['title', 'url', 'description', 'publish_date'])



def url(url):
  '''Takes an URL and returns a Feed'''
  return make(xml(url))


def make(src):
  '''Takes raw XML and constructs a new Feed'''
  return Feed(title=title(src), \
      eps=eps(src))


def xml(url):
  '''Takes a URL and returns the raw response, hopefully XML'''
  with req.urlopen(url) as resp:
    return ET.fromstring(resp.read())


def title(src):
  '''Finds and returns the title of a podcast'''
  return find('channel', src).find('title').text


def eps(src):
  '''Returns a list of Ep(isode)s'''
  return list(map(extract_ep, \
      find('channel', src).findall('item')))



def extract_ep(src):
  '''Extracts all episodes within src ET-object'''
  title = find_text('title', src)

  description = find_text('description', src)
  if description is None:
    description = find_text('media:description', src)

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
  f = find(attr, element)
  if f is not None:
    return f.text.strip('\n')
  else:
    return None

def find_url(attr, element):
  f = find(attr, element)
  if f is not None:
    return f.get('url', None)
  else:
    return None
