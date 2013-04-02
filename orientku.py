#!/usr/bin/python
import sys
import os
import urllib
from haikufinder import HaikuFinder
from xml.dom import minidom

#pull random articles from "volume CXLII" of the Orient
content = urllib.urlopen("http://bowdoinorient.com/api/xml_issuelist/CXLII")
issues = minidom.parse(content)
dates = issues.getElementById('0')
print dates

text = "the nation's oldest continuously published college newspaper"
usedlines = open("used.txt", "r").read()

#find the haikus
haikus = HaikuFinder(text).find_haikus()
for haiku in haikus:
	if(haiku[0] not in usedlines and haiku[1] not in usedlines and haiku[2] not in usedlines):
	        #tweet tweet motherfuckers
		new = "t update \"%s \n     %s \n%s\"" %(haiku[0],haiku[1],haiku[2])
                #os.system(new)

	        #blacklist all thre lines you just tweeted
		used = "echo \"%s\">>used.txt && echo \"%s\">>used.txt && echo \"%s\">>used.txt" %(haiku[0],haiku[1],haiku[2])
		os.system(used)
