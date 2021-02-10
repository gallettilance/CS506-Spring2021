def convert_type(item):
    types=[int,float]
    for type in types:
        try:
            return type(item)
        except ValueError:
            return item.strip('\"')

    


def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    result=[]
    with open (csv_file_path, 'r') as file:
        
        lines = file.readlines()
        for line in lines:
            dataset = line.rstrip().split(sep=',')
            row=[]
            for data in dataset:
                row.append(convert_type(data))
            result.append(row)
        return result 
        
