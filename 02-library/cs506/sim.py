def euclidean_dist(x, y):
    if x==[] or y==[]:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    if x==[] or y==[]:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    if x==[] or y==[]:
        raise ValueError("lengths must not be zero")
    set_x = set(x)
    set_y = set(y)

    intersect = set_x & set_y
    union = set_x | set_y
    return 1 - (len(intersect) / len(union))


def dot_product(x, y):
    if x==[] or y==[]:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    res = 0
    for i in range(len(x)):
        res += x[i] * y[i]
    return res


def norm(x):
    if x==[]:
        raise ValueError("lengths must not be zero")
    res = 0
    for i in range(len(x)):
        res += x[i] **2
    return res**(1/2)


def cosine_sim(x, y):
    if x==[] or y==[]:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    norm_multiple = norm(x) * norm(y)
    if norm_multiple == 0:
        raise ValueError("norm cannot be zero")
    return dot_product(x, y) / norm_multiple


def minkowski_distance(x, y, p):
    if x==[] or y==[]:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    if p < 1:
        raise ValueError("p must be bigger or equal to 1")
    res = 0
    for i in range(len(x)):
        res += (abs(x[i] - y[i])) ** p
    return res ** (1 / p)


# Feel free to add more
