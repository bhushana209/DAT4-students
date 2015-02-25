# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 16:13:20 2015

@author: Jason
"""

import re
import requests
import urllib
import zipfile

# Download the USPTO bulk download webpage and set regex pattern for urls
r = requests.get("https://www.google.com/googlebooks/uspto-patents-grants-text.html")
re_tag = re.compile("http://storage\.googleapis\.com/patents/grant_full_text/\d+/i?pg\d+\.zip")

# Create a list of the relevant urls
zips = re.findall(re_tag, r.text)

# Download and extract the zipfiles
destinationPath = '../data/USPTO_zipfiles/'

for url in zips:
    filename =  url[59:]
    try:
        urllib.urlretrieve(url, filename)
    except ValueError:
        continue
    sourceZip = zipfile.ZipFile(filename, 'r')
        
    for name in sourceZip.namelist():
        sourceZip.extract(name, destinationPath)
    sourceZip.close

'''
Test a small group to see if it works
for i in range(5):
    filename =  zips[i][59:]
    try:
        urllib.urlretrieve(zips[i], filename)
    except ValueError:
        continue
    sourceZip = zipfile.ZipFile(filename, 'r')
        
    for name in sourceZip.namelist():
        sourceZip.extract(name, destinationPath)
    sourceZip.close
'''