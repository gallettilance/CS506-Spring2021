def convert_type(x):
    types = [int, float]
    for t in types:
        try:
            ret = t(x)
            return ret
        except ValueError:
            pass
    return str(x).strip('\"')

def read_csv(csv_file_path):
    matrix = []
    with open(csv_file_path, "r") as f:
        for l in f.readlines():
            line = []
            for m in l.strip('\n').split(','):
                line.append(convert_type(m))
            matrix.append(line)
    return matrix