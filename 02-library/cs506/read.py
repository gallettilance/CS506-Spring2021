def read_csv(csv_file_path):

    with open(csv_file_path) as f:
        f=f.readlines()
        f_stripped=[]
        for line in f:
            line.strip("\n")
            f_stripped.append(line)
    return f_stripped
