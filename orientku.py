import sys
import os
import urllib
import json
import random
from haikufinder import HaikuFinder


## LET IT BE KNOWN that this was the second Python program I ever wrote.
## Don't judge me, bro.


tweeted = 0

while not tweeted:
    # pick a volume
    try:
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
        # text = "the nation's \"oldest\" continuously published college newspaper"
        # text = open("sometextfile.txt").read()

        url = "http://bowdoinorient.com/article/" + sectiontext[randarticle]["id"]
        print "Searching %s for haikus..." %url

        #text file keeps track of lines we've used
        usedlines = open("/home/bjacobel/projects/orientku/used.txt", "r").read()

        #find the haikus
        haikus = HaikuFinder(text).find_haikus()

        #pick a random one if more than one was found
        trycount = 0

        if haikus:
            print "%s haikus found in this article. Trying to tweet one of them..." %len(haikus)
            while (not tweeted) and (trycount <= len(haikus)):
                trycount += 1
                haiku = haikus[random.randrange(0, len(haikus), 1)]
                
                # parse double quotes
                haiku[0] = haiku[0].replace('"', '\\"')
                haiku[1] = haiku[1].replace('"', '\\"')
                haiku[2] = haiku[2].replace('"', '\\"')
                
                if(haiku[0] not in usedlines and haiku[1] not in usedlines and haiku[2] not in usedlines):
                    # tweet tweet motherfuckers
                    new = "twitter set \"%s \n     %s \n%s\n%s\"" %(haiku[0],haiku[1],haiku[2],url)
                    os.system(new)

                    # blacklist all the lines you just tweeted
                    # Like I said earlier.... don't judge me for this.
                    used = "echo \"%s\" >> ~/projects/orientku/used.txt && echo \"%s\" >> ~/projects/orientku/used.txt && echo \"%s\" >> ~/projects/orientku/used.txt" %(haiku[0],haiku[1],haiku[2])
                    os.system(used)
                    tweeted = 1
                    print "Tweeted!"
            if not tweeted:
                print "The only found tweet was already tweeted :("
        else:
            print "No haikus found :("

    except IndexError:
        #print "gracefully handled an IndexError"
        raise
    except ValueError:
        #print "gracefully handled a ValueError"
        raise
