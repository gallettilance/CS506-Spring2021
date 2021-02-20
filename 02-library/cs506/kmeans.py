from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    dimensino_point = len(points[0])
    for pt in points:
        if len(pt) != dimensino_point:
            raise ValueError("points are not in the same dimension")
    res = ()
    for j in range(dimensino_point):
        x = [p[j] for p in points]
        res.append(sum(x)/dimensino_point)
    return res

        


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    res = []
    for l in assignments:
        curlist = [elem for elem in l]
        cur_points = [dataset[i] for i in curlist]
        res.append(point_avg(cur_points))

    return res


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
    res = 0
    for i in range(len(a)):
        res += (a[i] - b[i])**2
    return res**(1/2)

def distance_squared(a, b):
    res= distance(a,b)
    return res**2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    return random.sample(dataset, k)

def cost_function(clustering):
    res = 0
    for cluster in clustering:
        cur_center = point_avg(cluster)
        for i in cluster:
            res+=distance(cur_center, i)
    return res


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    selected_centroid = []
    # first centroid is randomly choosen
    first_select = random.choice(dataset)
    selected_centroid.append(first_select)
    # check the distance and gradually pick the rest
    while len(selected_centroid)<k:
        distancelist = []
        for point in dataset:
            curdist = []
            for eachselected in selected_centroid:
                curdist.append(distance(eachselected,point))
            curmin = min(curdist)
            curmin /= curmin.sum()
            distancelist.append((curmin,point))
        curselected = random.choice(dataset, p = curmin / np.sum(curmin))
        selected_centroid.append(curselected)

    return selected_centroid



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
