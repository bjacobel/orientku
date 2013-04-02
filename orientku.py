#!/usr/bin/python
import sys
import os
import pycurl
from haikufinder import HaikuFinder
from xml.dom import minidom

#pull random articles from "volume CXLII" of the Orient

class xmlresponse:
   def __init__(self):
       self.contents = ''

   def body_callback(self, buf):
       self.contents = self.contents + buf

if not os.path.exists("issuelist.xml"):
   x = xmlresponse()
   c = pycurl.Curl()
   c.setopt(c.URL, "http://bowdoinorient.com/api/xml_issuelist/CXLII")
   c.setopt(c.WRITEFUNCTION, x.body_callback)
   c.perform()
   c.close()
   os.system("touch issuelist.xml")
   xmlcat = "echo \"%s\" >> issuelist.xml" %(x.contents)
   os.system(xmlcat)

issues = minidom.parse("issuelist.xml")
print issues
#dates = xmlissuelist.getElementsById('0')
#print dates

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
