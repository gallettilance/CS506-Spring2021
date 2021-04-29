def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for a, b in zip(x, y):
        res += abs(a - b)
    return res

def jaccard_dist(x, y):
    assert type(x) == set and type(y) == set
    intersection = x & y
    return len(intersection) / (len(x) + len(y) - len(intersection))

def cosine_sim(x, y):
    dot = [a * b for a, b in zip(x, y)]
    x_norm = sum([p**2 for p in x]) ** (1/2)
    y_norm = sum([q**2 for q in y]) ** (1/2)
    return dot / (x_norm * y_norm)

# Feel free to add more
