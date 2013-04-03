Orientku
=========
Inspired by [Times Haiku], The New York Times' April Fools Day joke-cum-tech-art-project, I've done the same for the venerable publication closest to my heart, the [@bowdoinorient].

System
----------
Python sends requests to the Orient's PHP API (which I converted from XML to JSON while I was writing this, because it needed doing anyway). The JSON is decoded from UTF8 to ASCII, parsed in Python using [haikufinder], then sent to Twitter via [t], a Ruby gem. 

Find the results at [@orientku].



Credits
-----------

* [Times Haiku] - inspiration
* [@bjacobel] - dev work
* [@tophtucker] - API foundation
* [@bowdoinorient] - writing heartfelt poetry
* [haikufinder] - setting it free
* [t] - the cli twitter client


  [t]: http://sferik.github.com/t/
  [haikufinder]: https://github.com/jdf/haikufinder
  [@tophtucker]: http://twitter.com/tophtucker
  [@bjacobel]: http://twitter.com/bjacobel
  [@bowdoinorient]: http://twitter.com/bowdoinorient
  [@orientku]: http://twitter.com/orientku
  [Times Haiku]: http://haiku.nytimes.com
