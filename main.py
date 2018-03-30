from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import data_generator as d
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

gen = d.DataGenerator()

#gen.clearDatabase()
#gen.generateDatabase(0.5,200)

infected_list = gen.getInfectedList()
km = KMeans(n_clusters=4).fit_predict(infected_list)
plt.figure(figsize=(12, 12))
li = np.asarray(infected_list)

#pca = PCA(n_components=2) #2-dim ensional PCA
#transformed = pd.DataFrame(pca.fit_transform(infected_list))
#plt.scatter(transformed[:][0], transformed[:][1], label='Class 1', c=km)
#plt.title("Yellow Fever")
#plt.show()
r = gen.getClassType()
print(r)
gen.endConnection()



