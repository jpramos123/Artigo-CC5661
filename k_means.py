import numpy as np
import random as random
import math as math
import matplotlib as mp


class k_means:
    def __init__(self, num_dimension, num_klusters, num_lessons):
        self.num_dim = num_dimension
        self.num_klus = num_klusters
        self.num_lessons = num_lessons
        self.seeds = np.array([(1,2), (3,2),(2,4)])
        self.lessons = np.array([(4,1,0), (2,4,0),(6,1,0),(3,2,0),(8,2,0),(2,4,0),(2,4,0)])

        #np.random.uniform(1, 10, [self.num_lessons, self.num_dim]

    #Euclidian Distance Method,
    #Returning the distance of each seeds(Kluster required) from each lessons
    # arr_dist = [ seed_1 [dist_lesson_1, dist_lessons_2, ... , dist_lesson_n]
    #              seed_2 [dist_lesson_1, dist_lessons_2, ... , dist_lesson_n]]
    def eucl_dist(self, lessons, seeds):
        self.arr_dist = np.zeros((self.num_klus, self.num_lessons))
        sum_dist = 0
        k = 0
        for i in range(self.num_klus):
            for j in range(self.num_lessons):
                for n in range(self.num_dim - 1):
                    sum_dist = sum_dist + (seeds[i][n] - lessons[j][n])**2

                sum_dist = math.sqrt(sum_dist)
                self.arr_dist[i][j] = sum_dist
                sum_dist = 0
        return self.arr_dist

    def min_dist(self):
        self.count_minor = [0] * (self.num_klus)

        menor = 0
        for j in range(self.num_lessons):
            for i in range(self.num_klus):
                if arr_dist[i][j] <= arr_dist[menor][j]:
                    menor = i
            self.lessons[j][2] = menor
            self.count_minor[menor] += 1
            menor = 0

    def calc_medoid(self):

        for i in range(num_lessons):
            self.medoid = np.zeros((self.num_klus, self.num_dim))
            for i in range (self.count_minor[i]):
                for j in range(self.num_dim):
                    dim_num



# Lessons from the DB
num_lessons = 6

#Number of colummsarr_min
dim_num = 3

#Number of clusters
kluster_num = 3


arr = np.zeros((kluster_num, num_lessons))

km = k_means(dim_num, kluster_num, num_lessons)

arr_dist = km.eucl_dist(km.lessons, km.seeds)

arr_min = km.min_dist()