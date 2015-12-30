#!/usr/bin/python
#
#	remove subdomains and duplicates from Squid blacklist files 
#


#
#	settings
#

# where to operate
workDir = "/etc/unison-sync"

# this file contains the list of blaclist domain files
blackListFileList = "sanitize.files"

# where to write sanitized domain list
outputFile = "Sanitized.domains"



# work starts

import os
os.chdir(workDir)

domains = []	# domains from all files

print "\nCurrent workdir is", workDir
print "Reading domains from file..."

with open(blackListFileList) as f:
  content = f.readlines()
  for blfile in content:	# read files one by one
    blfile = blfile.strip()
    if os.path.isfile(blfile):
      print "  ", blfile
      with open(blfile) as bl:	# every line of files
        bldoms = map( str.strip, bl.readlines() )	# trim domains
        bldoms = map( str.lower, bldoms )	# lowercase domains
        for bldom in bldoms:
          domains.append( bldom.split(".")[::-1] )	# split domains to parts


print "Sanitizing..."

bldomains = []	# here unique values will come
prevdomain = ["non","existent"]

cnt=0
for domain in sorted(domains):
  diff = len(set(prevdomain)-set(domain))	# compare to the previous one
  if diff > 0 :	# it is not subdomain
    prevdomain = domain
    bldomains.extend([ ".".join(prevdomain[::-1]) ])
    cnt+=1


print "Writing", cnt, "domains to", outputFile
of = open(outputFile, "w");
of.write( "\n".join(bldomains) );
of.close()

print "Done."

