#!/usr/bin/python
import sys
import os
import urllib
import json
import random
from haikufinder import HaikuFinder

#pull a random article from "volume CXLII" of the Orient
content = urllib.urlopen("http://bowdoinorient.com/api/json_issuelist/CXLII").read()
dates = json.loads(content)
maxissue = 0
for date in dates:
	if (int(date['issue_number']) > maxissue):
		maxissue = int(date['issue_number'])
randissue = random.randrange(0, maxissue, 1)
randdate = dates[randissue]['issue_date']
nexturl = "http://bowdoinorient.com/api/json_fulltext/"+randdate+"/"+str(random.randrange(1,5,1))
content = urllib.urlopen(nexturl).read()
sectiontext = json.loads(content)
randarticle = random.randrange(0, len(sectiontext), 1)
text = sectiontext[randarticle]["body"].encode('ascii', 'ignore')

#text = "the nation's oldest continuously published college newspaper"

#text file keeps track of lines we've used
usedlines = open("used.txt", "r").read()

#find the haikus
haikus = HaikuFinder(text).find_haikus()

#pick a random one if more than one was found
tweeted = 0

if haikus:
	while not tweeted:
		haiku = haikus[random.randrange(0, len(haikus), 1)]
		if(haiku[0] not in usedlines and haiku[1] not in usedlines and haiku[2] not in usedlines):
	                #tweet tweet motherfuckers
			new = "t update \"%s \n     %s \n%s\"" %(haiku[0],haiku[1],haiku[2])
			os.system(new)

 	                #blacklist all the lines you just tweeted
			used = "echo \"%s\">>used.txt && echo \"%s\">>used.txt && echo \"%s\">>used.txt" %(haiku[0],haiku[1],haiku[2])
			os.system(used)
			tweeted = 1
