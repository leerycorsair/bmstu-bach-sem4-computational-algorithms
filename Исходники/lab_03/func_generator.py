X_START: float = 0.0
X_END: float = 10.0
STEP: float = 1.0
FILENAME = "data.txt"


def MY_FUNC(x: float) -> float:
    return x * x


def func_value(x: float, func) -> float:
    return func(x)


def func_get_data(x_l: float, x_r: float, step: float, func) -> list:
    data: list = []
    while x_l <= x_r:
        data.append([x_l, func_value(x_l, func)])
        x_l += step
    return data


def func_print_data(f_data: list, filename: str) -> None:
    f = open(filename, "w")
    for dot in f_data:
        f.write("{:0.3f} {:0.3f}\n".format(dot[0], dot[1]))
    f.close()


def generator() -> None:
    f_data = func_get_data(X_START, X_END, STEP, MY_FUNC)
    func_print_data(f_data, FILENAME)


generator()
