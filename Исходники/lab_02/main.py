
def data_read(filename):
    dots = []
    f = open(filename, "r")
    values = []
    x_dots = f.readline()
    x_dots = x_dots.replace("\n", "").split(" ")
    x_dots = [float(dot) for dot in x_dots]
    dots.append(x_dots)
    y_dots = f.readline()
    y_dots = y_dots.replace("\n", "").split(" ")
    y_dots = [float(dot) for dot in y_dots]
    dots.append(x_dots)
    for i in range(len(dots[1])):
        line = f.readline()
        line = line.replace("\n", "").split(" ")
        line = [float(dot) for dot in line]
        values.append(line)
    f.close()
    return dots, values


def data_print(dots, values):
    for i in range(len(dots)):
        if (i == 0):
            print("X:")
        else:
            print("\nY:")
        for dot in dots[i]:
            print(dot, end=" ")
    print("\nValues:")
    for row in values:
        for dot in row:
            print(dot, end=" ")
        print()


def find_dots(data, polinom_degree, func_arg):
    for i in range(len(data)-1):
        if (data[i] < func_arg and data[i+1] > func_arg):
            index = i
            break
    curr_dots = 0
    step = 0
    while curr_dots <= polinom_degree:
        if (index - step >= 0):
            left = index - step
            curr_dots += 1
        if (index + 1 + step < len(data) and curr_dots <= polinom_degree):
            right = index + 1 + step
            curr_dots += 1
        step += 1
    return left, right


def reduce_data(dots, values, polinom_degree_x, polinom_degree_y, x_arg, y_arg):
    x_left, x_right = find_dots(dots[0], polinom_degree_x, x_arg)
    y_left, y_right = find_dots(dots[1], polinom_degree_y, y_arg)
    dots[0] = dots[0][x_left:x_right+1:1]
    dots[1] = dots[1][y_left:y_right+1:1]
    tmp = []
    for i in range(y_left, y_right+1, 1):
        tmp.append(values[i][x_left:x_right+1:1])
    values = tmp
    return dots, values


def newtone_func_value(data, func_arg):
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

    func_value = coefficients[0]
    curr_x = 1
    for i in range(len(data)-1):
        curr_x *= (func_arg - data[i][0])
        func_value += coefficients[i+1]*curr_x
    return func_value


def func_value(dots, values, polinom_degree_x, polinom_degree_y, x_arg, y_arg):
    dots, values = reduce_data(
        dots, values, polinom_degree_x, polinom_degree_y, x_arg, y_arg)
    interpolated_x = []
    for i in range(polinom_degree_y+1):
        tmp_data = [(dots[0][j], values[i][j])
                    for j in range(polinom_degree_x+1)]
        interpolated_x.append(newtone_func_value(tmp_data, x_arg))
    # print(interpolated_x)
    tmp_data = [(dots[1][j], interpolated_x[j])
                for j in range(polinom_degree_y+1)]
    return newtone_func_value(tmp_data, y_arg)


def main():
    filename = input("Data file:")
    dots, values = data_read(filename)
    data_print(dots, values)
    polinom_degree_x = int(input("Polinom degree X:"))
    polinom_degree_y = int(input("Polinom degree Y:"))
    x_arg = float(input("X value:"))
    y_arg = float(input("Y value:"))
    for i in range(1, 4):
        for j in range(1, 4):
            tmp_dots = dots.copy()
            tmp_values = values.copy()
            print("Nx = ", i, "Ny = ", j, "Func value = ", func_value(
                tmp_dots, tmp_values, i, j, x_arg, y_arg))
    func = func_value(dots, values, polinom_degree_x,
                      polinom_degree_y, x_arg, y_arg)
    print("Function value = ", func)


if (__name__ == "__main__"):
    main()
