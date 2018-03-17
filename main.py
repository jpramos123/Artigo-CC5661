from . import k_means as km

# Lessons from the DB
num_lessons = 7

#Number of columms
dim_num = 4

#Number of clusters
kluster_num = 5

k_M = km.k_means(dim_num, kluster_num, num_lessons)

arr_dist = k_M.eucl_dist(k_M.lessons, k_M.seeds)
