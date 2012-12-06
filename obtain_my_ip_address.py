import urllib2
import re


content = urllib2.urlopen('http://www.whatismyip.com/').read()
print content
