#!/usr/bin/env python

#URL Extrator.
print "A tool to extract links from a given URL."

import urllib2
from bs4 import BeautifulSoup
from urllib2 import Request, urlopen, URLError

try:
    url = str(raw_input('Enter URL: '))
    if not url:
        raise ValueError('No URL was provided!')
except ValueError as e:
    print(e)
    exit()

req = Request(url)

try:
    response = urlopen(req)
except URLError, e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code

v = "outputView"
p = "printView"

answer = raw_input('[p]rint or [v]iew ')

resp = urllib2.urlopen(url)
soup = BeautifulSoup(resp.read(), from_encoding=resp.info().getparam('charset'))

if answer in p:
    fo = open('output.txt', 'wb')
    for link in soup.find_all('a', href=True):
        fo.write( link['href'] + "\n");
    fo.close() # Close opened file
elif answer in v:
    for link in soup.find_all('a', href=True):
        print link['href']
else:
   print('Please respond with [p]rint or [v]iew ')

print 'bye'