import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


plt.figure(figsize=(12, 12))

#n_samples = 1500
#random_state = 170
#, y = make_blobs(n_samples=n_samples, random_state=random_state)

X = np.genfromtxt('data_set.csv', delimiter=',')

km = KMeans(n_clusters=3)

kmp = km.fit_predict(X)

wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.subplot(221)
plt.plot(range(1, 11), wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')

plt.subplot(222)
plt.scatter(X[:, 0], X[:, 1], c=kmp)
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:,1], s = 100, c = 'red', label = 'Centroids')
plt.title("K-means centroids")
plt.show()