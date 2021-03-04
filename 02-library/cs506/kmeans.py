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
    
    length=len(points[0])
    res=[]
    for i in range(length):
        res.append([])
    for i in range(len(points)):
        for ind_item in range(len(points[i])):
            res[ind_item].append(points[i][ind_item])
    for i in range(len(res)):
        sum=0
        for j in range(len(res[i])):
            sum+=res[i][j]
        res[i]=sum/len(res[i])
    return res
    
        





def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    new_centers=[]
    k=len(set(assignments))
    for i in range(k):
        new_centers.append([])
    for i in range(k):
        for j in range(len(assignments)):
            if assignments[j]==i:
                new_centers[i].append(dataset[j])
    for ind_each in range(len(new_centers)):
        new_centers[ind_each]=point_avg(new_centers[ind_each])
    return new_centers


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
    dis = sim.euclidean_dist(a,b)
    return dis

def distance_squared(a, b):
    dist = sim.euclidean_dist(a,b)
    return (dist**2)


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    res=random.sample(dataset,k)
    return res

def cost_function(clustering):
    k=len(clustering.keys())
    res=0
    for i in range(k):
        center=point_avg(clustering[i])
        for j in clustering[i]:
            temp=distance_squared(j,center)
            res+=temp
    return res

def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    centers=[]
    
    first_center=random.choice(dataset)
    centers.append(first_center)
    for i in range(k-1):
        compare=[]
        previous_center=centers[i]
        for ind_item in range(len(dataset)):
            temp=distance_squared(dataset[ind_item],previous_center)
            compare.append(temp)
        res_compare=sorted(compare)
        larger_dis=res_compare[-1]
        centers.append(dataset[compare.index(larger_dis)])
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
