from sklearn.cluster import KMeans
import data_generator as d

from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt


gen = d.DataGenerator()

#gen.generateInfected(1,0.5,2)
#gen.generateInfected(2,0.5,2)
#gen.generateInfected(3,0.5,2)
#gen.generateInfected(4,0.5,2)

infected_list = gen.getInfectedList()
km = KMeans(n_clusters=4).fit_predict(infected_list)
#print(km.cluster_centers_)
plt.figure(figsize=(12, 12))
li = np.asarray(infected_list)

plt.scatter(li[:,0], li[:, 19], c=km)
plt.scatter(li[:,0],li[:,1], c='red')
plt.scatter(li[:,0],li[:,2], c='blue')
plt.scatter(li[:,0],li[:,3], c='yellow')
plt.scatter(li[:,0],li[:,4], c='green')
plt.scatter(li[:,0],li[:,5], c='gray')
plt.scatter(li[:,0],li[:,6], c='brown')
plt.title("Yellow fever")
plt.show()