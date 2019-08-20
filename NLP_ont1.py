import math
import numpy as np
from scipy.spatial import distance
from sklearn.metrics.pairwise import cosine_similarity
import pdb
# get input from user

embeds_list = {}

with open("corpus_embeddings_file.txt") as f:
    for line in f:
        items = line.split()
        word = items[0]
        vec = items[1:]
        embeds_list[word] = vec
    
#read avg_ont file
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

#read from user
#sent = "congenital malformation of the left heart"
sent = "Congenital defect with failure of the development of the cerebral white matter"
#sent = "An erosion or abrasion of the cornea's outermost layer of epithelial cells"
strList = sent.split()


count_dict={}
for words in strList:

    if words in count_dict:

       count_dict[words] = count_dict[words] + 1
    else:
       count_dict[words] = 1

freq={}
IC={}
for k in count_dict:
    key = k
    value = count_dict[k] / float(len(count_dict))
    freq[key] = value
    IC[key] = - math.log(value, 2)


avg_sent= []
vecs_list = []
for word2 in strList:
    if word2 in embeds_list:
        feat_vec = np.array(embeds_list[word2], dtype='float32')
        ic_val = IC[word2]
        feat_vec = np.append(feat_vec, ic_val)
        feat_vec = feat_vec / np.linalg.norm(feat_vec) 
        vecs_list.append(feat_vec)

avg_vec = np.average(vecs_list, axis=0)
avg_sent.append(avg_vec)



ont_defs = np.array(classes_list.values(), dtype = 'float32')


dists = cosine_similarity(avg_sent,ont_defs)
sorted_dists = np.argsort(dists)[::-1][0]
#pdb.set_trace()

labels = []
top10 = sorted_dists[:10]
for ind in top10:
   #pdb.set_trace()
   labels.append(indices[ind])

pdb.set_trace() 
#    if np.array_equal(sorted_dists,n):
#       print(classes_list[n])
