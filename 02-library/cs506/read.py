#lab2
def convert_str(s):
    types = [int, float]
    for t in types:
        try:
            return t(s)
        except ValueError:
            pass
    return str(s).strip("\"")

def read_csv(csv_file_path):
    res = []
    with open(csv_file_path,'r') as csv_file:
        lines = csv_file.readlines()
        for line in lines:
            row =[]
            values = line.strip("\n").split(',')
            for val in values: 
                row.append(convert_str(val))
            res.append(row)
    return res
