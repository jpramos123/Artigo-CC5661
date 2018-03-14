import numpy as np
import random as random
import math as math
import matplotlib as mp


#Euclidian Distance Method
def eucl_dist(seeds, lessons, num_klusters, num_lessons , num_dim):
    arr_dist = np.zeros((num_klusters, num_lessons))
    sum_dist = 0
    k = 0
    for i in range(num_klusters):
        for j in range(num_lessons):
            for n in range(num_dim):
                sum_dist = sum_dist + (seeds[i][n] - lessons[j][n])**2

            sum_dist = math.sqrt(sum_dist)
            arr_dist[i][j] = sum_dist
            sum_dist = 0
    return arr_dist
#Number of columms
dim_num = 4

#Number of clusters
kluster_num = 5

#Randon generated seeds
seeds = np.random.uniform(1, 10, [kluster_num, dim_num])

#Lessons from the DB
num_lessons = 7
lessons = np.random.uniform(1, 10, [num_lessons, dim_num])

arr_dist = eucl_dist(seeds, lessons, kluster_num, num_lessons, dim_num)