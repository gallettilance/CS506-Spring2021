def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    X = []
    try:
        f = open(csv_file_path, 'r')

    except OSError as err:
        print(err)
        return

    with f:
        for row in f:
            X.append(row.split(','))

    return X


if __name__ == '__main__':
    f = open("../tests/test_files/dataset_2.csv", 'r')
    for row in f:
        #print(row.split(','))
        print(row.split(',')[0])
        #print(type(row.split(',')[1]))
