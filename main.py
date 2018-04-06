from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import data_generator as d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
import accuracy as ac


i = 1

gen = d.DataGenerator()

plt.figure(figsize=(12, 12))

gen.clearDatabase()
gen.generateDatabase(1*5/100, 20)

infected_list = np.array(gen.getInfectedList())
km = KMeans(n_clusters=5, n_init=1000, algorithm="full", tol=1e-8)
kmp = km.fit_predict(infected_list)

li = np.asarray(infected_list)
pca = PCA(n_components=2) #2-dim ensional PCA
transformed = pd.DataFrame(pca.fit_transform(infected_list))
cent_reduc = pd.DataFrame(pca.fit_transform(km.cluster_centers_))


plt.subplot(320+i)
plt.scatter(transformed[:][0], transformed[:][1], s = 20, c=kmp)
plt.scatter(cent_reduc[:][0], cent_reduc[:][1], s = 60, c = 'red', label = 'Centroids')
plt.tight_layout(3)
plt.title("{}% of Noise".format(i*5))
plt.legend()
#plt.draw()


a = np.array(gen.getPatterns())
code_ac = ac.accuracy(km.cluster_centers_, a)
eucl = code_ac.eucl_dist()
dist = code_ac.min_dist()
#perc = code_ac.percentage(dist, kmp)
print(dist)


r = gen.getClassType()

print(r)
print(kmp+1)
#perc = 0
#for i in range(len(r)):
#	if r[i] == (kmp[i]+1):
#		perc+=1
#print(perc/800*100)


plt.show()
gen.endConnection()


