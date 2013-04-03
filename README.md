Orientku
=========
Inspired by [Times Haiku], The New York Times' April Fools Day joke-cum-tech-art-project, I've done the same for the venerable publication closest to my heart, the [@bowdoinorient].

System
----------
Python requests JSON from the Orient's PHP API (which I converted from XML to JSON while I was writing this, because it needed doing anyway). The JSON is parsed parsed in Python using [haikufinder], then sent to Twitter via [t], a Ruby gem. Find the beautiful, poetic results at [@orientku].



Credits
-----------

* [Times Haiku] - inspiration
* [@bjacobel] - dev work 
* [@bowdoinorient] - heartfelt poetry
* [haikufinder] - setting poetry free
* [t] - a truly tireless twitterbot



License
-
MIT

  [t]: http://sferik.github.com/t/
  [haikufinder]: https://github.com/jdf/haikufinder
  [@bjacobel]: http://twitter.com/bjacobel
  [@bowdoinorient]: http://twitter.com/bowdoinorient
  [@orientku]: http://twitter.com/orientku
  [Times Haiku]: http://haiku.nytimes.com
