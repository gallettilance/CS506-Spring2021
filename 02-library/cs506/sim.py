def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i]) ** 2
    return res ** (1 / 2)


def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])
    return res
    # raise NotImplementedError()


def jaccard_dist(x, y):
    intersection = len(list(set(x).intersection(set(y))))
    union = (len(x) + len(y)) - intersection
    return 1 - float(intersection) / union


# raise NotImplementedError()

def cosine_sim(x, y):
    dot = sum(a * b for a, b in zip(x, y))
    norm_x = sum(a * a for a in x) ** 0.5
    norm_y = sum(b * b for b in y) ** 0.5
    return dot / (norm_x * norm_y)


def jaccard_sim(x, y):
    intersection = len(list(set(x).intersection(set(y))))
    union = (len(x) + len(y)) - intersection
    return float(intersection) / union
