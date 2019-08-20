

from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import squareform, pdist

import re
import numpy as np
import math
from sklearn.preprocessing import normalize


import numpy as np
import pandas as pd
import pdb
from utils import (
    get_hpo_ontology,
    get_hpo_set,
    get_anchestors,
    )



hpo = get_hpo_ontology('hp.obo')
heart_morph = get_hpo_set(hpo, 'HP:0001627')
#print (heart_morph)


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

listofdef = ont_def.values()

# words count
count_dict = {}

for countdeff in listofdef:
    worddefflist = countdeff.split(" ")

    listOfMatchedWods = set(worddefflist)

    for keyasWord in listOfMatchedWods:
        key = keyasWord
        if key in count_dict:

            count_dict[key] = count_dict[key] + 1
        else:
            count_dict[key] = 1

freq = {}
IC = {}

for k in count_dict:
    key = k
    value = count_dict[k] / float(len(ont_def))
    freq[key] = value
    IC[key] = - math.log(value, 2)

# dict for the word and its 200 vectors
word_embds = {}
f = open('/home/qabbaasa/Documents/summer_project/data/corpus_embeddings_file.txt')

for line in f:
    items = line.strip().split()
    word = items[0]
    vec = items[1:]
    word_embds[word] = vec

avg_ontdef = {}
for ont_class in ont_def:
    defintion = ont_def[ont_class].split()
    vecs_list = []
    for word in defintion:
        if word in word_embds:
            feat_vec = np.array(word_embds[word], dtype='float32')
            ic_val = IC[word]
            feat_vec = np.append(feat_vec, ic_val)
            feat_vec = feat_vec / np.linalg.norm(feat_vec)  # normalize
            vecs_list.append(feat_vec)

    avg_vec = np.average(vecs_list, axis=0)
    avg_ontdef[ont_class] = avg_vec

vectors = avg_ontdef.values()

ids = avg_ontdef.keys()


##########
ont_name = {}
f1 = open('/home/qabbaasa/Documents/summer_project/hp.obo', 'r')
for line in f1:
    if line.startswith('id:'):
        item = line.strip().split(" ")
        key = item[1]

    else:

        if line.startswith('name:'):
            items = line.strip().split(" ")
            newline = " ".join(items[1:])
            ont_name[key] = newline
        else:
            continue


# writ avg_ont_def to file
with open('/home/qabbaasa/Documents/summer_project/data/ont_def.txt', "a") as f:
    for i in avg_ontdef.keys():
        f.write(i+" "+' '.join([str(x) for x in avg_ontdef[i]]) + "\n")

#plotting the heart morph tree
heart_morph_dict = {}
for heart_class in heart_morph:
    if heart_class in avg_ontdef:
        vec = avg_ontdef[heart_class]
        heart_morph_dict[heart_class] = vec

heart_morph_dict1 = {}
for ids in heart_morph_dict:
    if ids in ont_name:
        name = ont_name[ids]
        vec1 = heart_morph_dict.values()
        heart_morph_dict1[name] = vec1  


# pdb.set_trace()

sub_vecs = heart_morph_dict.values()
u= np.asarray(sub_vecs)
sub_ids = heart_morph_dict.keys()
sub_names = heart_morph_dict1.keys()

similarities = cosine_similarity(u)
d= 1-similarities
Z = hierarchy.linkage(d,'average')
plt.figure(figsize=(150,80), facecolor=None, edgecolor=None, linewidth=(1.0),frameon=None, tight_layout= True)

plt.title('Hierarchical Clustering Dendrogram Heart Morphology')
plt.xlabel('Ontology Class')
plt.ylabel('Distance')
#plt.xticks( sub_names, rotation=23, ha = 'right', fontsize = 10)
dn = hierarchy.dendrogram(Z,labels=sub_ids,leaf_rotation =90.,leaf_font_size=10.) #,leaf_font_size= 10)

plt.savefig('heart_morph_average.pdf')
plt.show()

#print(similarities)
#print(Z)



###plotting the tree using euclidean/cosin###
#similarities = squareform(pdist(u,'euclidean'))
#linkage = hierarchy.linkage(similarities)

#dendro  = hierarchy.dendrogram(linkage,labels=sub_ids)
#plt.figure(figsize=(100,60), facecolor=None, edgecolor=None, linewidth=(1.0))
#plt.show()
#plt.savefig('heart_morph.pdf')