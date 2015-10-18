import unittest

from lib import feed

class FeedTest(unittest.TestCase):

  def setUp(self):
    self.urls = ['http://feeds.wnyc.org/radiolab', \
        'http://feeds.feedburner.com/freakonomicsradio']

  def test_scanUrl(self):
    for url in self.urls:
      f = feed.scan(url)
      self.assertEqual(f.url, url)
  
  def test_title(self):
    f = feed.scan(self.urls[0])
    self.assertTrue(isinstance(f.title, str))

  def test_eps(self):
    f = feed.scan(self.urls[0])
    
    for ep in f.eps:
      self.assertTrue(isinstance(ep.title, str))

if __name__ == '__main__':
  unittest.main()
