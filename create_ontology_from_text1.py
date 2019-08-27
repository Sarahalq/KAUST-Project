
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import squareform, pdist

import re
import numpy as np
import math
from sklearn.preprocessing import normalize



# step 1
# extracting the def from the ontology and writing it in a new file

ont_def = {}
f1 = open('/home/qabbaasa/Documents/summer_project/hp.obo', 'r')
for line in f1:
    if line.startswith('id:'):
        item = line.strip().split(" ")
        key = item[1]

    else:

        if line.startswith('def:'):
            items = line.strip().split(" ")
            items = " ".join(items[1:])
            newline = " ".join(re.split("[^a-zA-Z]*", items)).strip().lower()
            ont_def[key] = newline
        else:
            continue



# dict for the word and its 200 vectors
word_embds = {}
f = open('/home/qabbaasa/Documents/summer_project/data/corpus_embeddings_file.txt')

for line in f:
    items = line.strip().split()
    word = items[0]
    vec = items[1:]
    word_embds[word] = vec
#print(word_embds.get('hemithorax'))

avg_ontdef = {}
for ont_class in ont_def:
    defintion = ont_def[ont_class].split()
    vecs_list = []
    for word in defintion:
        if word in word_embds:
            feat_vec = np.array(word_embds[word], dtype='float32')
            vecs_list.append(feat_vec)

    avg_vec = np.average(vecs_list, axis=0)
    avg_ontdef[ont_class] = avg_vec


vectors = avg_ontdef.values()
ids = avg_ontdef.keys()

#print(avg_ontdef)
# writ avg_ont_def to file
with open('/home/qabbaasa/Documents/summer_project/data/ont_def.txt', "a") as f:
     for i in avg_ontdef.keys():
         f.write(i+" "+' '.join([str(x) for x in avg_ontdef[i]]) + "\n")


classes_list = {}
indices = {}
count = 0
with open("ont_def.txt") as f:
    for line in f:
        items = line.split()
        id1 = items[0]
        vec = items[1:]
        classes_list[id1] = vec
        indices[count] = id1
        count = count + 1           
#print(classes_list.get('HP:0001651'))
#read from user

sent = "Reduced ability to walk"

strList = sent.split()


avg_sent= []
vecs_list = []
for word2 in strList:
    if word2 in word_embds:
        feat_vec = np.array(word_embds[word2], dtype='float32')
        vecs_list.append(feat_vec)

avg_vec1 = np.average(vecs_list, axis=0)
avg_sent.append(avg_vec1)



ont_defs = np.array(classes_list.values(), dtype = 'float32')


dists = cosine_similarity(avg_sent,ont_defs)
sorted_dists = np.argsort(dists)[::-1][0]
#pdb.set_trace()

labels = []
top10 = sorted_dists[:10]

#print(top10)
for n in top10:
    labels.append(indices[n])
print(labels)