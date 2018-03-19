import numpy as np
import random as random
import math as math
import matplotlib as mp
<<<<<<< HEAD
from   database import infected
=======
import time
import copy
>>>>>>> master

start_time = time.time()

class k_means:
<<<<<<< HEAD
    def __init__(self, klusters):
        self.infected = infected.query()
        self.num_dim = self.infected['dimensions']
        self.num_klus = klusters
        self.num_lessons = self.infected['lessons']
        self.seeds = np.random.uniform(1, 10, [self.num_lessons, self.num_dim])
        self.lessons = self.infected['results']
=======
    def __init__(self, num_dimension, num_klusters, num_lessons):
        self.num_dim = num_dimension
        self.num_klus = num_klusters
        self.num_lessons = num_lessons
        self.seeds = np.random.uniform(1, 10, [self.num_klus, self.num_dim])
        self.old_seed = copy.deepcopy(self.seeds)
        self.lessons = np.random.uniform(1, 10, [self.num_lessons, self.num_dim])
        self.medoid = np.zeros((self.num_klus, self.num_dim))
        self.old_medoid = copy.deepcopy(self.medoid)


        self.ecd = 0
        self.md = 0
        self.cm = 0
        #np.random.uniform(1, 10, [self.num_lessons, self.num_dim])
>>>>>>> master

    #Euclidian Distance Method,
    #Returning the distance of each seeds(Kluster required) from each lessons
    # arr_dist = [ seed_1 [dist_lesson_1, dist_lessons_2, ... , dist_lesson_n]
    #              seed_2 [dist_lesson_1, dist_lessons_2, ... , dist_lesson_n]]
    def eucl_dist(self, lessons, seeds):
        self.arr_dist = np.zeros((self.num_klus, self.num_lessons))
        sum_dist = 0
<<<<<<< HEAD
#        k = 0
=======
        self.ecd += 1
>>>>>>> master
        for i in range(self.num_klus):
            for j in range(self.num_lessons):
                for n in range(self.num_dim - 1):
                    sum_dist = sum_dist + (seeds[i][n] - lessons[j][n])**2

                sum_dist = math.sqrt(sum_dist)
                self.arr_dist[i][j] = sum_dist
                sum_dist = 0
                if self.ecd == 1:
                    self.old_seed = copy.deepcopy(self.arr_dist)
        return self.arr_dist

<<<<<<< HEAD
    def min_dist(self):
#        arr_minor = np.zeros((self.num_klus, self.num_lessons, self.num_dim))
#        count_minor = [0] * (self.num_klus)
=======
>>>>>>> master

    def min_dist(self):
        self.count_minor = [0] * (self.num_klus)
        self.md += 1
        menor = 0
        for j in range(self.num_lessons):
            for i in range(self.num_klus):
                if arr_dist[i][j] <= arr_dist[menor][j]:
                    menor = i
<<<<<<< HEAD
            self.lessons[menor][4] = menor
            count_minor[menor] += 1
        return arr_minor
=======
            self.lessons[j][2] = menor   ##### NAO MUDA O KLUSTER RELACIONADO ########
                                         #### MESMO COM AS DISTANCIAS ALTERANDO ####
            self.count_minor[menor] += 1
            menor = 0


    def calc_medoid(self):
        self.medoid = np.zeros((self.num_klus, self.num_dim))
        self.cm += 1
        for i in range(self.num_lessons):
            for j in range(self.num_klus):
                if self.lessons[i][2] == j:
                    for k in range(self.num_dim - 1):
                        self.medoid[j][k] += self.lessons[i][k] / self.count_minor[j]
        if np.array_equal(self.old_medoid, self.medoid):
            return True
        self.old_medoid = copy.deepcopy(self.medoid)
        return False



#       s
#   4 2 0  l0
#   2 1 1  l1
#   5 2 1  l2
#   4 2 0  l3
#
#       #


# Lessons from the DB
lessons_num = 10000

#Number of colummsarr_min
dim_num = 23

#Number of clusters
kluster_num = 5

km = k_means(dim_num, kluster_num, lessons_num)

arr_dist = km.eucl_dist(km.lessons, km.seeds)

arr_min = km.min_dist()

medoid = km.calc_medoid()

finish = False
while(finish == False):
    dist = km.eucl_dist(km.lessons, km.medoid)
    min_dist = km.min_dist()
    finish = km.calc_medoid()

print("--- %s seconds ---" % (time.time() - start_time))
>>>>>>> master
