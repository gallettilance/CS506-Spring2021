import numpy as np 

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    return sum(abs(a-b) for a, b in zip(x,y))

def jaccard_dist(x, y):
    intersect = x.intersection(y)
    return float(len(intersect) / len(x)+len(y) - len(intersect))

def cosine_sim(x, y):
    return np.dot(x,y)/(np.norm(x)*np.norm(y))

# Feel free to add more
