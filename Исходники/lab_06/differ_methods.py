from data import FunctionData


def f_der_value(y1: float, y2: float, st: float) -> float:
    return (y2 - y1) / st


def s_der_value(y1: float, y2: float, y3: float, st: float) -> float:
    return (y1 - 2 * y2 + y3) / st


class Derivative():
    def __init__(self):
        self.values: list[float] = []

    def clear(self):
        self.values.clear()

    def prnt(self):
        for value in self.values:
            print("{:10.5f}".format(value), end=' ')
        print()

    def left(self, data: FunctionData):
        st = data.X[1] - data.X[0]
        for i in range(len(data.Y)):
            if i > 0:
                value = f_der_value(data.Y[i - 1], data.Y[i], st)
            else:
                value = float('NaN')
            self.values.append(value)

    def right(self, data: FunctionData):
        st = data.X[1] - data.X[0]
        for i in range(len(data.Y)):
            if i < len(data.Y) - 1:
                value = f_der_value(data.Y[i], data.Y[i + 1], st)
            else:
                value = float('NaN')
            self.values.append(value)

    def center(self, data: FunctionData):
        st = 2 * (data.X[1] - data.X[0])
        for i in range(len(data.Y)):
            if i > 0 and i < len(data.Y) - 1:
                value = f_der_value(data.Y[i - 1], data.Y[i + 1], st)
            else:
                value = float('NaN')
            self.values.append(value)

    def runge_left(self, data: FunctionData):
        st = (data.X[1] - data.X[0])
        for i in range(len(data.Y)):
            if i > 1:
                d1 = f_der_value(data.Y[i - 1], data.Y[i], st)
                d2 = f_der_value(data.Y[i - 2], data.Y[i], 2 * st)
                value = 2 * d1 - d2
            else:
                value = float('NaN')
            self.values.append(value)

    def runge_right(self, data: FunctionData):
        st = (data.X[1] - data.X[0])
        for i in range(len(data.Y)):
            if i < len(data.Y) - 2:
                d1 = f_der_value(data.Y[i], data.Y[i + 1], st)
                d2 = f_der_value(data.Y[i], data.Y[i + 2], 2 * st)
                value = 2 * d1 - d2
            else:
                value = float('NaN')
            self.values.append(value)

    def align_var(self, data: FunctionData):
        for i in range(len(data.Y)):
            if i < len(data.Y) - 1:
                eta_ksi_diff = (1 / data.Y[i + 1] - 1 / data.Y[i]) / (
                    1 / data.X[i + 1] - 1 / data.X[i])
                value = eta_ksi_diff * data.Y[i]**2 / data.X[i]**2
            else:
                value = float('NaN')
            self.values.append(value)

    def scnd_diff(self, data: FunctionData):
        st = (data.X[1] - data.X[0])**2
        for i in range(len(data.Y)):
            if i > 0 and i < len(data.Y) - 1:
                value = s_der_value(data.Y[i - 1], data.Y[i], data.Y[i + 1],
                                    st)
            else:
                value = float('NaN')
            self.values.append(value)


def differ_methods(data: FunctionData) -> None:

    deriv = Derivative()

    methods = [
        deriv.left, deriv.right, deriv.center, deriv.runge_left,
        deriv.runge_right, deriv.align_var, deriv.scnd_diff
    ]

    for method in methods:
        print("{:15}".format(method.__name__), end=" ")
        method(data)
        deriv.prnt()
        deriv.clear()
