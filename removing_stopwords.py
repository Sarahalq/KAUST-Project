#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 18:09:36 2017

@author: qabbaasa
"""
#%%
from nltk.corpus import stopwords  
StopWords = stopwords.words('english')
data= '/home/qabbaasa/Documents/summer_project/data/' ##the path
inputfile = data+'medline_abstracts.txt'
outputfile = data+'preprocessed_abstracts1.txt'

  
with open(inputfile) as f1:   
    f = open(outputfile,'w') 
    for line in f1:
        line = ' '.join([word for word in line.split() if word not in StopWords])
        line = line.lower()
        f.write(line+'\n')
    f.close()    
#%%
import nltk
nltk.download('all')