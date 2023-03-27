def newtone_data_read(filename):
    data = []
    f = open(filename, "r")
    for line in f:
        line = (line.replace("\n", "")).split(" ")
        line[0] = float(line[0])
        line[1] = float(line[1])
        data.append(line)
    f.close()
    print("Data was read.")
    return data


def newtone_data_print(data):
    print("|{0:^10}|{1:^10}|".format("x", "y"))
    for row in data:
        print("|{0:^10}|{1:^10}|".format(row[0], row[1]))


def newtone_find_dots(data, polinom_degree, func_arg):
    for i in range(len(data)-1):
        if (data[i][0] < func_arg and data[i+1][0] > func_arg):
            index = i
            break
    curr_dots = 0
    dots = []
    step = 0
    while curr_dots <= polinom_degree:
        if (index - step >= 0):
            dots.insert(0, data[index-step])
            curr_dots += 1
        if (index + 1 + step < len(data) and curr_dots <= polinom_degree):
            dots.append(data[index+1+step])
            curr_dots += 1
        step += 1
    return dots


def newtone_func_value(data, polinom_degree, func_arg):
    data = newtone_find_dots(data, polinom_degree, func_arg)
    coefficients = []
    curr_col = []
    curr_col_i = 1
    for row in data:
        curr_col.append(row[1])

    coefficients.append(curr_col[0])
    new_col = []
    while (len(curr_col) > 1):
        for i in range(len(curr_col)-1):
            new_col.append((curr_col[i]-curr_col[i+1]) /
                           (data[i][0]-data[i+curr_col_i][0]))
            if (i == 0):
                coefficients.append(new_col[0])
        curr_col_i += 1
        curr_col = new_col.copy()
        new_col.clear()

    print("Coefficients list: ", *coefficients)
    func_value = coefficients[0]
    curr_x = 1
    for i in range(len(data)-1):
        curr_x *= (func_arg - data[i][0])
        func_value += coefficients[i+1]*curr_x
    return func_value


def newtone_func_root(data, polinom_degree):
    for row in data:
        row[0], row[1] = row[1], row[0]
    data.sort()
    func_root = newtone_func_value(data, polinom_degree, 0.0)
    return func_root


def newtone_perform():
    filename = input("Data file:")
    data = newtone_data_read(filename)
    newtone_data_print(data)
    polinom_degree = int(input("Polinom degree:"))
    func_arg = float(input("Function argument:"))
    func_value = newtone_func_value(data, polinom_degree, func_arg)
    print("Newtone polinom value = ", func_value)
    func_root = newtone_func_root(data, polinom_degree)
    print("Func root = ", func_root)
