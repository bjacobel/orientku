#!/usr/bin/python
import sys
import os
from haikufinder import HaikuFinder


text = "the nation's oldest continuously published college newspaper"
usedlines = open("used.txt", "r").read()

haikus = HaikuFinder(text).find_haikus()
for haiku in haikus:
	if(haiku[0] not in usedlines and haiku[1] not in usedlines and haiku[2] not in usedlines):
	        #tweet tweet
		new = "t update \"%s \n     %s \n%s\"" %(haiku[0],haiku[1],haiku[2])
                #os.system(new)

	        #blacklist all thre lines you just tweeted
		used = "echo \"%s\">>used.txt && echo \"%s\">>used.txt && echo \"%s\">>used.txt" %(haiku[0],haiku[1],haiku[2])
		os.system(used)
