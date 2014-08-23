__author__ = 'FSebile'
 
import urllib2
import re
import sys
reload (sys)
sys.setdefaultencoding('utf-8')
d=1
from BeautifulSoup import BeautifulSoup
url="http://en.wikipedia.org/wiki/List_of_universities_in_Turkey"
page=urllib2.urlopen(url)
soup=BeautifulSoup(page.read())
isim=soup.fetch('a',{'href':re.compile('/wiki/'),'title':re.compile(' University')})
for link in isim:
print d, link
d+=1
