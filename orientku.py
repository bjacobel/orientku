#!/usr/bin/python
import sys
import os
from haikufinder import HaikuFinder


text = "the nation's oldest continuously published college newspaper"

haikus = HaikuFinder(text).find_haikus()
for haiku in haikus:
	cmd = "t update \"%s \n     %s \n%s\"" %(haiku[0],haiku[1],haiku[2])
	os.system(cmd)
