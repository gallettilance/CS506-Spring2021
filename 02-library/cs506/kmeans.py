from collections import defaultdict
from math import inf
import random
import csv
from cs506 import sim


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    dim = len(points[0])
    avg = [0 for x in range(dim)]

    for i in range(len(points)):
        avg = [avg[j] + points[i][j] for j in range(dim)]

    return [avg[k] / len(points) for k in range(dim)]


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    k = len(set(assignments))
    centers = [[] for i in range(k)]

    for i in range(len(assignments)):
        ind = assignments[i]
        centers[ind] += [dataset[i]]

    return [point_avg(center) for center in centers]


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


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    return sim.euclidean_dist(a, b)


def distance_squared(a, b):
    return distance(a, b) ** 2


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return random.sample(dataset, k)


def cost_function(clustering):
    k = len(clustering)
    res = 0

    for i in range(k):
        center = point_avg(clustering[i])
        norms = 0
        for p in clustering[i]:
            norms = distance_squared(p, center)

        res += norms

    return res


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    centers = [random.choice(dataset)]

    distances = [[distance_squared(centers[0], p), p] for p in dataset]
    distances.sort(reverse=True)

    i = 1
    while i < k:
        centers.append(distances[i - 1][1])
        i += 1
    
    return centers


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