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
usage: pyphoid [-h] [-d DOWNLOAD] [-l LAST_ONE]

optional arguments:
  -h, --help            show this help message and exit
  -d DOWNLOAD, --download DOWNLOAD
  -l LAST_ONE, --last-one LAST_ONE
```
## Two modes

### hmm i'm not sure about this podcast
```
$ pyphoid -l http://feeds.feedburner.com/freakonomicsradio

Getting the last episode on URL: http://feeds.feedburner.com/freakonomicsradio
(0/1) => Freakonomics Radio/Is Migration a Basic Human Right?.mp3
All good in the hood? True
```

### i <3 this podcast
```
$ pyphoid.py -d http://feeds.feedburner.com/freakonomicsradio

Catching up with podcast on URL: http://feeds.feedburner.com/freakonomicsradio
Downloading episodes...
ERR: "Freakonomics Radio/Is Migration a Basic Human Right?.mp3" already exists
(1/250) => Freakonomics Radio/The Cheeseburger Diet.mp3
(2/250) => Freakonomics Radio/Ben Bernanke Gives Himself a Grade.mp3
[...]
All good in the hood? True
```

# Tests

e.g.

```
$ python3 lib/*_test.py
```

/v.
