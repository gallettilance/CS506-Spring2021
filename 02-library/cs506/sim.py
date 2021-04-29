
def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    dif=[]
    try:
        if len(x)!=len(y):
            raise ValueError
        for p,q in zip(x,y):
            dif.append(abs(p-q))
        return(sum(dif))
    except ValueError:
        print('x and y mush have equal dimensions')
def jaccard_dist(x, y):
    s1 = set(x)
    s2 = set(y)
    try:
        dist= 1-(float(len(s1.intersection(s2)) / len(s1.union(s2))))
    except ZeroDivisionError:
        dist=0

    return dist
def cosine_sim(x, y):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(x)):
        x1 = x[i]; y1 = y[i]
        sumxx += x1*x1
        sumyy += y1*y1
        sumxy += x1*y1

    try:
        sim=sumxy/((sumxx*sumyy)**.5)
    except ZeroDivisionError:
        sim=0
    return sim

# Feel free to add more
