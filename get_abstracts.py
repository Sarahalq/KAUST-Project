#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:57:17 2017

@author: qabbaasa
"""
#%%
import gzip
from bs4 import BeautifulSoup
import sys

args = sys.argv 
inputfile= args[1]
outputfile = args[2]

a=gzip.open(inputfile)
file_content=a.read()
soup = BeautifulSoup(file_content, "lxml-xml")

titles = soup.find_all('ArticleTitle')
abstracts = soup.find_all('AbstractText')

with open(outputfile, 'a') as f:
    for title, absrtact in zip(titles, abstracts):
        print title.get_text()
        f.write(title.get_text().encode('utf-8')+ '\n')

        print absrtact.get_text()
        f.write(absrtact.get_text().encode('utf-8')+ '\n')
        #break

#titles = soup.find_all('AbstractText')