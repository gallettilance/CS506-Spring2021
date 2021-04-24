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

    intersect_x_y = set_x & set_y
    union_x_y = set_x | set_y
    return 1 - len(intersect_x_y)/len(union_x_y)


def dot(x,y):
    return (sum(a*b for a,b in zip(x,y)))


def cosine_sim(x, y):
    if x==[] or y==[]:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    denominator = ((dot(x,x)**0.5) * (dot(y,y)**0.5))
    if denominator == 0:
        raise ValueError("denominator cannot be zero")
    # a . b = |a| * |b| * cost<a,b>
    # cos<a,b> = (a,b)/(|a|*|b|)
    return dot(x,y)/denominator

# Feel free to add more
