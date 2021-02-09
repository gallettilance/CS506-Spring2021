def euclidean_dist(x, y):
    if x == [] or y == []:
        raise ValueError("lengths must be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    if x == [] or y == []:
        raise ValueError("lengths must be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    if x == [] or y == []:
        raise ValueError("lengths must be zero")

    raise NotImplementedError()

def cosine_sim(x, y):
    if x == [] or y == []:
        raise ValueError("lengths must be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    raise NotImplementedError()

# Feel free to add more
