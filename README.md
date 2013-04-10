Orientku
=========
Inspired by [Times Haiku], The New York Times' April Fools Day joke-cum-tech-art-project, I've done the same for the [@bowdoinorient].

System
----------
Python sends requests to the Orient's PHP API (which I converted from XML to JSON while I was writing this, because it needed doing anyway). The returned JSON is decoded, cleaned up, parsed in Python using [haikufinder], then sent to Twitter via [t], a Ruby gem. The script is activated every three hours between 9am and 9pm by cron - the only manual interaction in the entire system is when I run it manually 'cuz I'm bored.

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

License
-------------------
IDGAF. Feel free to use in any way you'd like so long as you don't violate the licenses of [t] or [haikufinder].