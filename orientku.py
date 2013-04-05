#!/usr/bin/python
import sys
import os
import urllib
import json
import random
from haikufinder import HaikuFinder

tweeted = 0

while not tweeted:
	#pikc a volume
        content = urllib.urlopen("http://bowdoinorient.com/api/json_volumelist").read()
        volumes = json.loads(content)
	volume = volumes[random.randrange(0,len(volumes))]["roman"]

        #pull a random article from that volume of the Orient
	content = urllib.urlopen("http://bowdoinorient.com/api/json_issuelist/"+str(volume)).read()
	dates = json.loads(content)
	maxissue = 0
	for date in dates:
		if (int(date['issue_number']) > maxissue):
			maxissue = int(date['issue_number'])
	randissue = random.randrange(0, maxissue)
	randdate = dates[randissue]['issue_date']
	nexturl = "http://bowdoinorient.com/api/json_fulltext/"+randdate+"/"+str(random.randrange(1,5,1))
	content = urllib.urlopen(nexturl).read()
	sectiontext = json.loads(content)
	randarticle = random.randrange(0, len(sectiontext))
	text = sectiontext[randarticle]["body"].encode('ascii', 'ignore')

	url = "http://bowdoinorient.com/article/" + sectiontext[randarticle]["id"]
	print "Searching %s for haikus..." %url

        #text = " the nation's oldest continuously published college newspaper"

        #text file keeps track of lines we've used
	usedlines = open("used.txt", "r").read()

        #find the haikus
	haikus = HaikuFinder(text).find_haikus()

        #pick a random one if more than one was found
	trycount = 0

	if haikus:
		print "%s haikus found in this article. Trying to tweet one of them..." %len(haikus)
		while (not tweeted) and (trycount <= len(haikus)):
			trycount+=1
			haiku = haikus[random.randint(0, len(haikus))]
			if(haiku[0] not in usedlines and haiku[1] not in usedlines and haiku[2] not in usedlines):
	                        #tweet tweet motherfuckers
				new = "t update \"%s \n     %s \n%s\n%s\"" %(haiku[0],haiku[1],haiku[2],url)
				os.system(new)

 	                        #blacklist all the lines you just tweeted
				used = "echo \"%s\">>used.txt && echo \"%s\">>used.txt && echo \"%s\">>used.txt" %(haiku[0],haiku[1],haiku[2])
				os.system(used)
				tweeted = 1
				print "Tweeted!"
		if not tweeted:
			print "The only found tweet was already tweeted :("
	else:
		print "No haikus found :("

