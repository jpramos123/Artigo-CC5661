import numpy as np
import math as math


class accuracy:

    def __init__(self, clusters, patterns):
        self.num_dim = np.shape(clusters)[1]
        self.num_klus = np.shape(clusters)[0]
        self.num_lessons = np.shape(patterns)[0]
        self.seeds = clusters
        self.patterns = patterns

    #Euclidian Distance Method,
    #Returning the distance of each seeds(Kluster required) from each lessons
    # arr_dist = [ seed_1 [dist_lesson_1, dist_lessons_2, ... , dist_lesson_n]
    #              seed_2 [dist_lesson_1, dist_lessons_2, ... , dist_lesson_n]]

    def eucl_dist(self):
        self.arr_dist = np.zeros((self.num_klus, self.num_lessons))
        sum_dist = 0
        for i in range(self.num_klus):
            for j in range(self.num_lessons):
                for n in range(self.num_dim):
                    sum_dist = sum_dist + (self.seeds[i][n] - self.patterns[j][n]) ** 2

                sum_dist = math.sqrt(sum_dist)
                self.arr_dist[i][j] = sum_dist
                sum_dist = 0

    def min_dist(self):
        self.count_minor = [0] * (self.num_klus)
        vec_min = []
        menor = 0
        for j in range(self.num_lessons):
            for i in range(self.num_klus):
                if self.arr_dist[i][j] <= self.arr_dist[menor][j]:
                    menor = i
            vec_min.append(menor)
            self.count_minor[menor] += 1
            menor = 0
        vm = np.array(vec_min)
        return vm

    def percentage(self, dist, km):
        size = np.shape(dist)[0]
        count = 0
        for i in range (size):
            if dist[i] == km[i]:
                count += 1
        return (count / size) * 100
