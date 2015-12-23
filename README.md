Pyphoid
=======

Pyphoid requires URLs to feed.

# Installation
```
$ git clone git@github.com:varl/pyphoid.git /path/to/pyphoid
$ chmod +x /path/to/pyphoid.py
$ ln -s /path/to/pyphoid.py ~/bin/pyphoid
```

# Usage
```
$ pyphoid -h

usage: pyphoid [-h] [-d] [-l] url

positional arguments:
  url              URL to the podcast feed (RSS/XML)

optional arguments:
  -h, --help       show this help message and exit
  -d, --download
  -l, --last-only
```
## Three modes

### `--last-only` hmm i'm not sure about this podcast
```
$ pyphoid -l http://feeds.feedburner.com/freakonomicsradio

Getting the last episode on URL: http://feeds.feedburner.com/freakonomicsradio
(0/1) => Freakonomics Radio/2015-12-16T23:00:00-05:00_Is Migration a Basic Human Right?.mp3
All good in the hood? True
```

### `--download` i <3 this podcast
```
$ pyphoid.py -d http://feeds.feedburner.com/freakonomicsradio

Catching up with podcast on URL: http://feeds.feedburner.com/freakonomicsradio
ERR: "Freakonomics Radio/2015-12-16T23:00:00-05:00_Is Migration a Basic Human Right?.mp3" already exists
(1/250) => Freakonomics Radio/2015-12-09T23:00:00-05:00_The Cheeseburger Diet.mp3
(2/250) => Freakonomics Radio/2015-12-02T23:00:00-05:00_Ben Bernanke Gives Himself a Grade.mp3
(3/250) => Freakonomics Radio/2015-11-25T23:00:00-05:00_Why Do People Keep Having Children? (Rebroadcast).mp3
[...]
All good in the hood? True
```

### `--interactive` i'll decide as i go

Shows the title and some more information about the episode before choosing to download it or not.

```
$ pyphoid -i http://feeds.feedburner.com/freakonomicsradio

Using interactive mode to retrieve episodes on URL: http://feeds.feedburner.com/freakonomicsradio
ERR: "Freakonomics Radio/2015-12-16T23:00:00-05:00_Is Migration a Basic Human Right?.mp3" already exists
[...]
(171/250) => Freakonomics Radio/2012-09-05T16:00:00-04:00_Can Selling Beer Cut Down on Public Drunkenness?.mp3

Title:          Can Selling Beer Cut Down on Public Drunkenness?
Published:      2012-09-05T16:00:00-04:00
URL:            http://feedproxy.google.com/~r/freakonomicsradio/~5/x44C-2hZZco/freakonomics_mppodcast090512.mp3
Description:    Can Selling Beer Cut Down on Public Drunkenness?
--------
Download (y/n)?
```

# Tests

e.g.

```
$ python3 lib/*_test.py
```

/v.
