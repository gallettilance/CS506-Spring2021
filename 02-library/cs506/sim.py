def euclidean_dist(x, y):
    if x==[] or y==[]:
        raise ValueError("lengths must not be zero")
    if len(x)!=len(y):
        raise ValueError("lengths must be equal")
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    if x==[] or y==[]:
        raise ValueError("lengths must not be zero")
    if len(x)!=len(y):
        raise ValueError("lengths must be equal")
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])**1
    return res*(1/1)

def jaccard_dist(x, y):
    if x==[] or y==[]:
        raise ValueError("lengths must not be zero")
    setx = set(x)
    sety = set(y)
    union = setx|sety
    inters = setx&sety
    return (1-len(inters)/len(union))


def multi(x,y):
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    res = 0
    for i in range(len(x)):
        res += x[i]*y[i]
    return res

def norm(x):
    if x == []:
        raise ValueError("lengths must not be zero")
    res=0
    for each in range(len(x)):
        res += x[each]**2
    return res**(1/2)


def cosine_sim(x, y):
    if x==[] or y==[]:
        raise ValueError("lengths must not be zero")
    if len(x)!=len(y):
        raise ValueError("lengths must be equal")
    return multi(x,y)/(norm(x)*norm(y))

# Feel free to add more
