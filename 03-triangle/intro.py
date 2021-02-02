triangle = []
with open("./triangle.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        nums = [int(x) for x in line.split(" ")]
        triangle.append(nums)

def add_list(x, y):
    if len(x) != len(y):
        raise ValueError
    res = []
    for i in range(len(x)):
        res.append(x[i]+ y[i])
    return res

def max_list(x, y):
    if len(x) != len(y):
        raise ValueError
    res = []
    for i in range(len(x)):
        res.append(max([x[i], y[i]]))
    return res

def get_max_path_sum(triangle):
    x = triangle[0]
    for i in range(1, len(triangle)):
        y = triangle[i]
        addx0y = add_list(x + [0], y)
        add0xy = add_list([0] + x, y)
        maxSumAtStepi = max_list(add0xy, addx0y)
        x = maxSumAtStepi
    return max(x)

print(get_max_path_sum(triangle))