Pyphoid
=======

Pyphoid requires URLs to feed.

# Installation
```
$ chmod +x /path/to/pyphoid.py
$ ln -s /path/to/pyphoid.py ~/bin/pyphoid
```

# Usage
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
