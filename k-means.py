import numpy as np
import random as random
import math as math

#Number of columms
n = 4
#Number of clusters
k = 5
#Randon generated seeds
seeds = np.random.uniform(1.0, 10.0, [k, n])

#Lessons from the DB
lessons = np.random.uniform(1.0, 10.0, [k, n])

arr_dist = np.zeros(k)
arr_min_dist = np.zeros((k, n))

for i in range(len(seeds)):
    for j in range(len(seeds[i])):
        arr_dist[i] = np.linalg.norm(seeds[i]-lessons[i])




