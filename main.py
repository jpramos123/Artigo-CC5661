from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import data_generator as d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from time import time
import analysis
gen = d.DataGenerator()

plt.figure(figsize=(12,12))
totalKMeansAcc = []
totalNoise = []
iterations = range(1,7)
print(iterations)
for i in iterations:
	gen.clearDatabase()
	gen.generateDatabase(i*10/100,5)

	initialTime = time()
	infected_list = gen.getInfectedList()
	km = KMeans(n_clusters=5, n_init=1000, algorithm="full", tol=1e-8)
	kmp = km.fit_predict(infected_list)
	duration = time() - initialTime
	print('K-Means duration: {}'.format(duration))

	# REMOVER inicio:

	#print(gen.getPatterns())
	#print(km.cluster_centers_)

	# REMOVER fim.

	li = np.asarray(infected_list)
	pca = PCA(n_components=2) #2-dim ensional PCA
	transformed = pd.DataFrame(pca.fit_transform(infected_list))
	cent_reduc = pd.DataFrame(pca.fit_transform(km.cluster_centers_))

	print(transformed) # REMOVER: impressão do vetor transformado dos infectados
	print(cent_reduc)  # REMOVER: impressão do vetor transformado dos centros de clusters

	plt.subplot(320+i)
	plt.scatter(transformed[:][0], transformed[:][1], s = 20, c=kmp, label = None)
	plt.scatter(cent_reduc[:][0], cent_reduc[:][1], s = 60, c = 'red', label = 'Centroids')
	plt.tight_layout(3)
	plt.title("{}% of Noise".format(i*10))
	plt.legend()
	plt.draw()

	classes = gen.getClassType()

	dbClustersOrigin = gen.getPatterns()
	#print(len(dbClustersOrigin))
	#print(len(km.cluster_centers_))
	#print(analysis.identifyCluster(dbClustersOrigin, km.cluster_centers_))
	#print(analysis.identifyCluster(dbClustersOrigin, km.cluster_centers_))
	#print(classes)
	#print(kmp+1)
	dbClusters = analysis.identifyCluster(km.cluster_centers_, dbClustersOrigin)
	perc = 0
	for i in range(len(kmp)):
		if kmp[i]+1 == dbClusters[classes[i]-1]:
			perc += 1
		#print('KMP : ',kmp[i]+1)
		#print('DBCF: ',dbClusters[classes[i]-1])

	accuracyPercentage = perc/len(kmp)*100

	print('Kmeans accuracy = {}%'.format(accuracyPercentage))

	totalKMeansAcc.append(accuracyPercentage)
	totalNoise.append(i*5/100)
	print(totalKMeansAcc,totalNoise)

	#print(r)
	#print(kmp+1)
	#perc = 0
	#for i in range(len(r)):
	#	if r[i] == (kmp[i]+1):
	#		perc+=1
	#print(perc/800*100)
plt.show()
plt.plot(totalNoise,totalKMeansAcc)
plt.show()
gen.endConnection()


