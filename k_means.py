import numpy as np
import random as random
import math as math
import matplotlib as mp
from   database import infected


class k_means:
    def __init__(self, klusters):
        self.infected = infected.query()
        self.num_dim = self.infected['dimensions']
        self.num_klus = klusters
        self.num_lessons = self.infected['lessons']
        self.seeds = np.random.uniform(1, 10, [self.num_lessons, self.num_dim])
        self.lessons = self.infected['results']

    #Euclidian Distance Method,
    #Returning the distance of each seeds(Kluster required) from each lessons
    # arr_dist = [ seed_1 [dist_lesson_1, dist_lessons_2, ... , dist_lesson_n]
    #              seed_2 [dist_lesson_1, dist_lessons_2, ... , dist_lesson_n]]
    def eucl_dist(self, lessons, seeds):
        self.arr_dist = np.zeros((self.num_klus, self.num_lessons))
        sum_dist = 0
#        k = 0
        for i in range(self.num_klus):
            for j in range(self.num_lessons):
                for n in range(self.num_dim):
                    sum_dist = sum_dist + (seeds[i][n] - lessons[j][n])**2

                sum_dist = math.sqrt(sum_dist)
                self.arr_dist[i][j] = sum_dist
                sum_dist = 0
        return self.arr_dist

    def min_dist(self):
#        arr_minor = np.zeros((self.num_klus, self.num_lessons, self.num_dim))
#        count_minor = [0] * (self.num_klus)

        menor = 0
        for j in range(self.num_lessons):
            for i in range(self.num_klus):
                if arr_dist[i][j] < arr_dist[menor][j]:
                    menor = i
            self.lessons[menor][4] = menor
            count_minor[menor] += 1
        return arr_minor
