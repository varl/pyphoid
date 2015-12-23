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
## Two modes

### `--last-only` hmm i'm not sure about this podcast
```
$ pyphoid -l http://feeds.feedburner.com/freakonomicsradio

Getting the last episode on URL: http://feeds.feedburner.com/freakonomicsradio
(0/1) => Freakonomics Radio/Is Migration a Basic Human Right?.mp3
All good in the hood? True
```

### `--download` i <3 this podcast
```
$ pyphoid.py -d http://feeds.feedburner.com/freakonomicsradio

Catching up with podcast on URL: http://feeds.feedburner.com/freakonomicsradio
Downloading episodes...
Catching up with podcast on URL: http://feeds.feedburner.com/freakonomicsradio
ERR: "Freakonomics Radio/2015-12-16T23:00:00-05:00_Is Migration a Basic Human Right?.mp3" already exists
(1/250) => Freakonomics Radio/2015-12-09T23:00:00-05:00_The Cheeseburger Diet.mp3
(2/250) => Freakonomics Radio/2015-12-02T23:00:00-05:00_Ben Bernanke Gives Himself a Grade.mp3
(3/250) => Freakonomics Radio/2015-11-25T23:00:00-05:00_Why Do People Keep Having Children? (Rebroadcast).mp3
[...]
All good in the hood? True
```

# Tests

e.g.

```
$ python3 lib/*_test.py
```

/v.
