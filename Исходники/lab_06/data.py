from dataclasses import dataclass


@dataclass
class FunctionData:
    X: list[float]
    Y: list[float]

    def __init__(self):
        self.X = []
        self.Y = []

    def append(self, x: float, y: float):
        self.X.append(x)
        self.Y.append(y)


def data_read(filename: str) -> FunctionData:
    data = FunctionData()

    f = open(filename, "r")
    for line in f:
        line = (line.replace("\n", "")).split(" ")
        x, y = [float(num) for num in line]
        data.append(x, y)
    f.close()

    return data


def data_print(data: FunctionData) -> None:
    for (x, y) in zip(data.X, data.Y):
        print("X = {:.3f}, Y = {:.3f}".format(x, y))
