import unittest

import feed

class FeedTest(unittest.TestCase):

  def setUp(self):
    self.urls = ['http://feeds.wnyc.org/radiolab', \
        'http://feeds.feedburner.com/freakonomicsradio']

  def test_convert(self):
    d1 = 'Thu, 26 Mar 2009 13:06:00 GMT'
    self.assertEqual(feed.convert(d1), '2009-03-26')

    d2 = 'Fri, 26 Feb 2016 16:40:40 +0000'
    self.assertEqual(feed.convert(d2), '2016-02-26')

  def test_title(self):
    f = feed.url(self.urls[0])
    self.assertTrue(isinstance(f.title, str))

  def test_eps(self):
    f = feed.url(self.urls[0])
    
    for ep in f.eps:
      self.assertTrue(isinstance(ep.title, str))

if __name__ == '__main__':
  unittest.main()
