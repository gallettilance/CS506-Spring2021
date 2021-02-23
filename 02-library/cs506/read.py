def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = []
    with open(csv_file_path, 'r') as csv_file:
        lines = csv_file.readlines()
        for line in lines:
            row = []
            values = line.strip('\n').split(',')
            for val in values:
                row.append(convert_str(val))
            res.append(row)

    return res


def convert_str(s):
    types = [int, float]
    for t in  types:
        try:
            return t(s)
        except ValueError:
            pass
    return str(s).strip('\"')

if __name__ == '__main__':
    f = open("../tests/test_files/dataset_2.csv", 'r')
    print(f.readline())
    #for row in f:
        #print(row.split(','))
        #print(row.split(','))
        #print(type(row.split(',')[1]))
