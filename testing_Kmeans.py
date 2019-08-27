#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 20:20:13 2017

@author: qabbaasa
"""
#%%
import gensim 
model = gensim.models.Word2Vec.load_word2vec_format('/home/qabbaasa/Documents/summer_project/medline_embeddings_file.txt',binary=True)

x= model.wv
#%%

dict = {}
with open('/home/qabbaasa/Documents/summer_project/data/embeddings_file1.txt') as f:
   for line in f:
      items = line.strip().split()
      word = items[0]
      vec = items[1:]
      dict[word] = vec
      
import numpy as np
myarray = np.asarray(dict)
print (myarray)
#np.array(list(X_train), dtype=np.float)

#%%
#x=np.array(myarray)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
from matplotlib import style#we can ignore it if we have python 2.7 because we will have the older version of the lib
style.use("ggplot")#we can ignore it if we have python 2.7 because we will have the older version of the lib
from sklearn.cluster import KMeans


kmean= KMeans(n_clusters=2, random_state=0).fit(dict)

#%%
centroids = Kmean.cluster_centers_
labels = Kmean.labels_

print (centroids) #the center points in the cluster 
print(labels) 