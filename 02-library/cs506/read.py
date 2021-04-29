def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    ans = []
    with open(csv_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            r = []
            words = line.strip('\n').split(',')
            for word in words:
                r.append(word)
            ans.append(r)

    return ans
