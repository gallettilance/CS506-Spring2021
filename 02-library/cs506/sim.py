def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    raise NotImplementedError()

def jaccard_dist(x, y):
    raise NotImplementedError()

def cosine_sim(x, y):
    raise NotImplementedError()

# Feel free to add more
