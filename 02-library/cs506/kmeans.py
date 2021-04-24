from collections import defaultdict
from math import inf
from random import random

import numpy as np
from numpy.linalg import norm


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    num = len(points[0])
    new_center = []
    for cnt in range(num):
        sum = 0
        for p in points:
            sum += p[cnt]
        new_center.append(float("%.6f" % (sum / float(len(points)))))
    return new_center


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    poss_clusters = defaultdict(list)
    centers = []
    for assignment, point in zip(assignments, dataset):
        poss_clusters[assignment].append(point)

    for points in poss_clusters.values():
        centers.append(point_avg(points))

    return centers

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments

def calc_min_dist(data_points, centers):
    """
    """
    min_dist_values = []
    for point in data_points:
        smallest = inf  # positive infinity
        dataset_idx = 0
        for i in range(len(centers)):
            val = distance_squared(point, centers[i])
            if val < smallest:
                smallest = val
        min_dist_values.append(smallest)
    return min_dist_values

def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    aa = np.array(a)
    bb = np.array(b)
    distant =  norm(aa-bb)
    return distant


def distance_squared(a, b):
    dst = distance(a,b) ** 2
    return dst


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    random_state=np.random.randint(0,2**32)
    np.random.seed(random_state)
    centroids = []
    size = len(dataset)

    for _ in range(k):
        random_center = np.random.randint(0, size)
        centroids.append(dataset[random_center])
    return centroids


def cost_function(clustering):
    k = len(clustering)
    centers = []
    for points in clustering.values():
        centers.append(point_avg(points))

    ds_dist = 0
    elem_cnt = 0
    for i in range(k):
        clust_dist = 0
        for j in range(len(clustering[i])):
            clust_dist += distance_squared(clustering[i][j], centers[i])
            elem_cnt  += 1
        ds_dist += clust_dist
    dataset_cost = (1/elem_cnt)*(ds_dist)
    return dataset_cost

def generate_centers_pp(dataset, centroids, k):
    random_state=np.random.randint(0,2**32)
    np.random.seed(random_state)
    new_centers = []
    for _ in range(1,k):
        sum_sqd = 0
        prob_array = []
        dist_sqds = calc_min_dist(dataset, centroids)
        for j in range(len(dist_sqds)):
            sum_sqd += dist_sqds[j]
        max_p = -inf
        min_p = inf
        for ds in range(len(dist_sqds)):
            prob_array.append(dist_sqds[ds] / sum_sqd)
            if (dist_sqds[ds]/ sum_sqd) > (max_p):
                max_p = dist_sqds[ds]/ sum_sqd
            if dist_sqds[ds]/ sum_sqd < min_p and dist_sqds[ds] != 0:
                min_p = dist_sqds[ds]/ sum_sqd
        goal = min_p + ((max_p - min_p)/2)
        select_rand = min_p
        incr = max_p - min_p/(len(dataset)-len(centroids))
        while select_rand < goal: select_rand = np.random.uniform(min_p, max_p)
        t = 0
        for q in range(len(prob_array)):
            incr = incr * (1+q)
            for p in range(len(prob_array)):
                if prob_array[p] < select_rand + incr and prob_array[p] > select_rand - incr:
                    t = p
                    break
            if prob_array[t] < select_rand + incr and prob_array[t] > select_rand - incr:
                break
        new_centers.append(dataset[t])

        return new_centers


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    random_state = np.random.randint(0, 2 ** 32)
    np.random.seed(random_state)
    centroids = []
    size = len(dataset)
    random_center = np.random.randint(0, size)
    centroids.append(dataset[random_center])

    if k > 1:
        point = generate_centers_pp(dataset, centroids, k)
        if point != []:
            centroids.append(point)
    if len(centroids) != k:
        remaining = k-len(centroids)
        for _ in range(remaining):
            random_center = np.random.randint(0, size)
            centroids.append(dataset[random_center])

    return centroids


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
