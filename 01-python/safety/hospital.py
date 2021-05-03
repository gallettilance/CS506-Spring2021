def draw_hospital():
    a_file = open("hos.txt")
    lines = a_file.readlines()
    for line in lines:
        print(line)
    return

draw_hospital()