#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:10:13 2017

@author: qabbaasa
"""


#%%
import gensim 

input_file =  "preprocessed_abstracts1.txt"
output_file =  "embeddings_file1.txt"


sents=gensim.models.word2vec.LineSentence(input_file)


model = gensim.models.word2vec.Word2Vec(sents,size=200, window=5, min_count=1, sg =1, workers = 10)

model.save_word2vec_format(output_file)
