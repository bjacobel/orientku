import os
import requests
import random
from haikufinder import HaikuFinder


## LET IT BE KNOWN that this was the second Python program I ever wrote.
## Don't judge me, bro.

USED_LOG = "./used.txt"

tweeted = False

volumes = requests.get("http://bowdoinorient.com/api/json_volumelist").json()[1:] # volume CXXXII doesn't actually have issues in it in the API

while not tweeted:
    # pick a volume
    volume = volumes[random.randrange(0,len(volumes))]["roman"]

    #pull a random article from that volume
    dates = requests.get("http://bowdoinorient.com/api/json_issuelist/"+str(volume)).json()

    maxissue = int(dates.pop()["issue_number"])

    randissue = random.randrange(0, maxissue)
    
    try:
        randdate = dates[randissue]['issue_date']
    except:
        print "I've made a terrible mistake. (Vol. {} no. {})\n".format(131 + int(volumes[random.randrange(0,len(volumes))]["id"]), randissue)
        continue
   
    nexturl = "http://bowdoinorient.com/api/json_fulltext/"+randdate+"/"+str(random.randrange(1,5,1))

    try:
        sectiontext = requests.get(nexturl, timeout=5).json()
    except requests.exceptions.Timeout:
        print "The API took too long to respond. Aborting this request."
    randarticle = random.randrange(0, len(sectiontext))
    text = sectiontext[randarticle]["body"].encode('ascii', 'ignore')

    url = "http://bowdoinorient.com/article/" + sectiontext[randarticle]["id"]
    print "Searching %s for haikus..." %url

    # text file keeps track of lines we've used
    usedlines = open(USED_LOG, "r").read()

    # find the haikus
    haikus = HaikuFinder(text).find_haikus()

    # pick a random one if more than one was found
    trycount = 0

    if haikus:
        print "%s haiku(s) found in this article. Trying to tweet one of them..." %len(haikus)
        while (not tweeted) and (trycount <= len(haikus)):
            trycount += 1
            haiku = haikus[random.randrange(0, len(haikus), 1)]
            
            # parse double quotes
            haiku[0] = haiku[0].replace('"', '\\"')
            haiku[1] = haiku[1].replace('"', '\\"')
            haiku[2] = haiku[2].replace('"', '\\"')
            
            if(haiku[0] not in usedlines and haiku[1] not in usedlines and haiku[2] not in usedlines):
                # tweet tweet motherfuckers
                new = 'twitter set "{} \n     {} \n{}\n{}"'.format(haiku[0], haiku[1], haiku[2], url)
                os.system(new)

                # blacklist all the lines you just tweeted
                # Like I said earlier.... don't judge me for this.
                used = 'echo "{line1}" >> {logfile} && echo "{line2}" >> {logfile} && echo "{line3}" >> {logfile}'.format(line1 = haiku[0], line2 = haiku[1], line3 = haiku[2], logfile = USED_LOG)
                os.system(used)
                tweeted = True
                print "Tweeted!"

        if not tweeted:
            print "That tweet was already tweeted :("
    else:
        print "No haikus found :("

    print ""
