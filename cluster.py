from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import sys

sys.setrecursionlimit(10000)

similarities = cosine_similarity(vectors[:20])
Z = hierarchy.linkage(similarities,'single')
plt.figure(figsize=(100,60), facecolor=None, edgecolor=None, linewidth=(1.0)
,frameon=None, tight_layout=None)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Ontology Class')
plt.ylabel('Distance')
dn = hierarchy.dendrogram(Z,labels=ids)
#plt.savefig('figure.pdf')