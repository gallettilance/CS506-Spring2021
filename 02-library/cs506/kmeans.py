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
    if len(points) == 0:
        return []
    else:
        centroid = []
        for i in range(len(points[0])):
            centroid.append(sum(p[i] for p in points) / len(points))
        return centroid


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    centroids = []
    clusters = set(assignments)

    for i in range(len(clusters)):
        points = []
        for j in range(len(dataset)):
            if assignments[j] == i:
                points.append(dataset[j])

        centroids.append(point_avg(points))

    return centroids


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
    if len(a) != len(b):
        raise ValueError("a and b must have the same length!")
    else:
        square_distance = 0
        for i in range(len(a)):
            square_distance += (b[i] - a[i]) ** 2
        return square_distance ** 0.5


def distance_squared(a, b):
    if len(a) != len(b):
        raise ValueError("a and b must have the same length!")

    else:
        square_distance = 0
        for i in range(len(a)):
            square_distance += (b[i] - a[i]) ** 2

        return square_distance


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    indices = [i for i in range(len(dataset))]
    random.shuffle(indices)
    res = []
    for i in range(k):
        res.append(dataset[indices[i]])

    return res


def cost_function(clustering):
    dist = 0

    for k in clustering.keys():
        centroid = point_avg(clustering[k])
        for point in clustering[k]:
            dist += distance_squared(point, centroid)

    return dist


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    centroids = random.choices(dataset, k = 1)

    # Initialize distance
    weight = []
    for point in dataset:
        weight.append(distance_squared(point, centroids[0]) ** 0.5)

    # Randomly select next k - 1 centroids with weights
    for i in range(1, k):
        centroids.append(random.choices(dataset, k = 1, weights = weight)[0])
        # Update weights
        for p in range(len(dataset)):
            weight[p] = min(weight[p], distance_squared(dataset[p], centroids[-1]))

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
    if k not in range(1, len(dataset) + 1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset) + 1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
