def convert_type(x):
    type_tests = [
        # (data type, cast test)
        (int, int),
        (float, float)
    ]
    for typ, test in type_tests:
        try:
            v = test(x)
            return v
        except ValueError:
            continue
    return str(x).strip('\"')

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    X = []
    with open(csv_file_path, "r") as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            new_line = []
            for x in line.split(','):
                v = convert_type(x)     
                new_line.append(v)
            X.append(new_line)    
    return X