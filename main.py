from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import data_generator as d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

gen = d.DataGenerator()

plt.figure(figsize=(12,12))

for i in range(1,7):
	gen.clearDatabase()
	gen.generateDatabase(i*5/100,10)

	infected_list = gen.getInfectedList()
	km = KMeans(n_clusters=4, n_init=1000, algorithm="full", tol=1e-8)
	kmp = km.fit_predict(infected_list)

	li = np.asarray(infected_list)
	pca = PCA(n_components=2) #2-dim ensional PCA
	transformed = pd.DataFrame(pca.fit_transform(infected_list))
	cent_reduc = pd.DataFrame(pca.fit_transform(km.cluster_centers_))
	plt.subplot(320+i)
	plt.scatter(transformed[:][0], transformed[:][1], s = 20, label='Class 1', c=kmp)
	plt.scatter(cent_reduc[:][0], cent_reduc[:][1], s = 60, c = 'red', label = 'Centroids')
	plt.tight_layout(3)
	plt.title("{}% of Noise".format(i*5))
	plt.legend()
	#plt.draw()

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


