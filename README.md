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

usage: pyphoid [-h] [-o OUTPUT_DIR] [-d | -l | -i] url

positional arguments:
  url                   URL to the podcast feed (RSS/XML)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory where the podcast show will be saved
  -d, --download        download available episodes
  -l, --last-only       only download the most recent episode
  -i, --interactive     pick what episodes to download (newest first)
```
## Three modes

### `--last-only` hmm i'm not sure about this podcast
```
$ pyphoid -l http://feeds.feedburner.com/freakonomicsradio

Getting the last episode on URL: http://feeds.feedburner.com/freakonomicsradio
(0/1) => Freakonomics Radio/2015-12-16_Is Migration a Basic Human Right?.mp3
All good in the hood? True
```

### `--download` i <3 this podcast
```
$ pyphoid -d -o /cygdrive/z/podcasts http://feeds.wnyc.org/radiolab

Catching up with podcast on URL: http://feeds.wnyc.org/radiolab
ERR: "/cygdrive/z/podcasts/Radiolab/2015-12-22_Year-End Special #1.mp3" already exists
ERR: "/cygdrive/z/podcasts/Radiolab/2015-12-18_The Fix.mp3" already exists
No URL for ep "The Cold War". Skipping...
(3/144) => /cygdrive/z/podcasts/Radiolab/2015-11-22_Birthstory.mp3
(4/144) => /cygdrive/z/podcasts/Radiolab/2015-11-02_Staph Retreat.mp3
(5/144) => /cygdrive/z/podcasts/Radiolab/2015-10-19_Update: New Normal?.mp3
(6/144) => /cygdrive/z/podcasts/Radiolab/2015-10-06_Smile My Ass.mp3
[...]
All good in the hood? True
```

### `--interactive` i'll decide as i go

Shows the title and some more information about the episode before choosing to download it or not.

```
$ pyphoid -i http://feeds.feedburner.com/freakonomicsradio

Using interactive mode to retrieve episodes on URL: http://feeds.feedburner.com/freakonomicsradio
ERR: "Freakonomics Radio/2015-12-16_Is Migration a Basic Human Right?.mp3" already exists
[...]
(171/250) => Freakonomics Radio/2012-09-05_Can Selling Beer Cut Down on Public Drunkenness?.mp3

Title:          Can Selling Beer Cut Down on Public Drunkenness?
Published:      2012-09-05
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
