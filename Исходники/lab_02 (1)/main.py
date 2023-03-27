
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


def reduce_data(dots, values, polinom_degree, x_arg, y_arg):
    x_left, x_right = find_dots(dots[0], polinom_degree, x_arg)
    y_left, y_right = find_dots(dots[1], polinom_degree, y_arg)
    dots[0] = dots[0][x_left:x_right+1:1]
    dots[1] = dots[1][y_left:y_right+1:1]
    tmp = []
    for i in range(y_left, y_right+1, 1):
        tmp.append(values[i][x_left:x_right+1:1])
    values = tmp
    return dots, values


def multi(max, args, arg_value):
    multi = 1
    for i in range(max):
        multi *= (arg_value - args[i])
    return multi


def div_dif(x_range, x_list, y_range, y_list, values):
    if len(x_range) == 1 and len(y_range) == 1:
        return values[x_range[0]][y_range[0]]
    if len(y_range) != 1:
        return (div_dif(x_range, x_list, y_range[0:-1], y_list[0:-1], values) - div_dif(x_range, x_list, y_range[1:], y_list[1:], values))/(y_list[0]-y_list[-1])
    return (div_dif(x_range[0:-1], x_list[0:-1], y_range, y_list, values) - div_dif(x_range[1:], x_list[1:], y_range, y_list, values))/(x_list[0]-x_list[-1])


def func_value(dots, values, polinom_degree, x_arg, y_arg):
    dots, values = reduce_data(dots, values, polinom_degree, x_arg, y_arg)
    func = 0
    for i in range(polinom_degree+1):
        for j in range(polinom_degree):
            dd = div_dif(list(range(0, i+1)),
                         dots[0][0:i+1], list(range(0, j+1)), dots[1][0:j+1], values)
            func += dd * multi(i, dots[0], x_arg) * multi(j, dots[1], y_arg)
    return func


def main():
    filename = input("Data file:")
    dots, values = data_read(filename)
    data_print(dots, values)
    polinom_degree = int(input("Polinom degree X:"))
    x_arg = float(input("X value:"))
    y_arg = float(input("Y value:"))
    func = func_value(dots, values, polinom_degree, x_arg, y_arg)
    print("Function value = ", func)


if (__name__ == "__main__"):
    main()
